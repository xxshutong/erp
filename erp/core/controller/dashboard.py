from django.shortcuts import render_to_response
from django.template import RequestContext
from erp.core.models import Machine

DASHBOARD_PAGE = 'dashboard.html'


def dashboard(request):
    machines = Machine.objects.all()
    return render_to_response(
        DASHBOARD_PAGE, {}, RequestContext(request, {
            'machines': machines,
        }),
    )