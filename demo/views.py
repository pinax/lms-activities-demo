from django.shortcuts import redirect, render

from account.decorators import login_required

from pinax.lms.activities.models import activities_for_user


def home(request):
    if request.user.is_authenticated():
        return redirect("dashboard")
    return render(request, "homepage.html")


@login_required
def dashboard(request):

    activities = activities_for_user(request.user)

    return render(request, "dashboard.html", {
        "activities": activities,
    })
