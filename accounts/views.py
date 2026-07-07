from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, LoginForm



def signup_view(request):

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("dashboard")

    else:

        form = SignupForm()


    return render(
        request,
        "accounts/signup.html",
        {
            "form": form
        }
    )



def login_view(request):

    if request.method == "POST":

        form = LoginForm(
            request,
            data=request.POST
        )


        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect("dashboard")


    else:

        form = LoginForm()



    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )



def logout_view(request):

    logout(request)

    return redirect("login")



@login_required
def profile_view(request):

    profile = request.user.profile


    current_level_xp = (profile.level - 1) * 100

    next_level_xp = profile.level * 100


    progress = profile.xp - current_level_xp


    progress_percent = int(
        (progress / 100) * 100
    )


    if progress_percent > 100:

        progress_percent = 100



    # Rank System

    if profile.level <= 2:

        rank = "👶 Beginner"


    elif profile.level <= 4:

        rank = "📘 Learner"


    elif profile.level <= 6:

        rank = "💻 Intermediate"


    elif profile.level <= 8:

        rank = "🚀 Advanced"


    elif profile.level <= 10:

        rank = "👑 Expert"


    else:

        rank = "🏆 Master"



    # Badge System

    badge_list = []


    if profile.total_attempts >= 1:

        badge_list.append("🎉 First Quiz")


    if profile.total_attempts >= 5:

        badge_list.append("📚 Learner")


    if profile.total_attempts >= 10:

        badge_list.append("💪 Dedicated")


    if profile.xp >= 500:

        badge_list.append("⭐ XP Master")


    if profile.streak >= 7:

        badge_list.append("🔥 Consistent")


    if profile.overall_average >= 90:

        badge_list.append("🎯 High Performer")



    return render(
        request,
        "accounts/profile.html",
        {
            "profile": profile,
            "progress_percent": progress_percent,
            "next_level_xp": next_level_xp,
            "rank": rank,
            "badge_list": badge_list,
        }
    )