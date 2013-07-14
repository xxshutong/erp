import datetime
from xmlrpclib import DateTime
from django.shortcuts import render_to_response
from django.template import RequestContext
from erp.core.models import Machine, Configuration

DASHBOARD_PAGE = 'dashboard.html'


def dashboard(request):
    machines = Machine.objects.all()
    configuration = Configuration.objects.all()[0]
    for machine in machines:
        if machine.end_time_estimated is not None:
            temp_end = machine.end_time_estimated - datetime.timedelta(days=configuration.notify_time_interval)
            machine.warn = datetime.datetime.utcnow() > temp_end.replace(tzinfo=None)
    return render_to_response(
        DASHBOARD_PAGE, {}, RequestContext(request, {
            'machines': machines,
        }),
    )