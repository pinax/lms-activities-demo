from django.shortcuts import redirect, render

from account.decorators import login_required

from pinax.lms.activities.models import get_activities


def home(request):
    if request.user.is_authenticated():
        return redirect("dashboard")
    return render(request, "homepage.html")


@login_required
def dashboard(request):

    activities = get_activities(request.user)

    return render(request, "dashboard.html", {
        "activities": activities,
    })
