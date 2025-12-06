from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

@login_required
def profile(request):
    user = request.user  # currently logged-in user

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Update user info
        user.username = username
        user.email = email
        user.save()  # <-- This is required to persist changes

        messages.success(request, "Your profile has been updated!")
        return redirect('profile')  # Redirect to avoid re-submission

    # GET request: show current user info
    return render(request, 'profile.html', {'user': user})
