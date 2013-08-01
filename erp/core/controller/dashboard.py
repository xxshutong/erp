# coding: utf-8
import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template import RequestContext
from erp.core.models import Machine, Configuration

DASHBOARD_PAGE = 'dashboard.html'


def dashboard(request):
    machines = Machine.objects.all().order_by('no')
    configuration = Configuration.objects.all()[0]
    # warn if close to end
    for machine in machines:
        # 计算预计产量
        if machine.speed and machine.wei_mi and machine.efficiency:
            timedelta = datetime.datetime.utcnow() - machine.start_time.replace(tzinfo=None)
            machine.output_estimated = timedelta.total_seconds() / 60 * machine.speed / machine.wei_mi / 100 * machine.efficiency

        # 计算是否即将到结束时间
        if machine.end_time_estimated is not None:
            temp_end = machine.end_time_estimated - datetime.timedelta(days=configuration.notify_time_interval)
            machine.warn = datetime.datetime.utcnow() > temp_end.replace(tzinfo=None)
            machine.error = datetime.datetime.utcnow() > machine.end_time_estimated.replace(tzinfo=None)

    paginator = Paginator(machines, configuration.page_size)

    # get page no
    page = request.GET.get('page')

    # get records of current page
    try:
        page_machines = paginator.page(page)
    except PageNotAnInteger:
        page_machines = paginator.page(1)
    except EmptyPage:
        page_machines = paginator.page(paginator.num_pages)

    return render_to_response(
        DASHBOARD_PAGE, {}, RequestContext(request, {
            'page_machines': page_machines,
        }),
    )