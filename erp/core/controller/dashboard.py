from django.shortcuts import render_to_response
from django.template import RequestContext

DASHBOARD_PAGE = '../views/dashboard.html'

def dashboard(request):
    return render_to_response(
        DASHBOARD_PAGE, {}, RequestContext(request, {
            'login_form': 'aa',
        }),
    )