from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


def signup_view(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('dashboard')

    else:

        form = SignupForm()

    return render(
        request,
        'accounts/signup.html',
        {'form': form}
    )


def login_view(request):

    if request.method == 'POST':

        form = LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('dashboard')

    else:

        form = LoginForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


def logout_view(request):

    logout(request)

    return redirect('login')


@login_required
@login_required
def profile_view(request):

    profile = request.user.profile

    current_level_xp = (profile.level - 1) * 100

    next_level_xp = profile.level * 100

    progress = profile.xp - current_level_xp

    progress_percent = int(
        (progress / 100) * 100
    )

    return render(
        request,
        "accounts/profile.html",
        {
            "profile": profile,
            "progress_percent": progress_percent,
            "next_level_xp": next_level_xp,
        },
    )