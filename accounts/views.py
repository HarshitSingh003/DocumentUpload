from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User


def user_login(request):
    # user = User.objects.create_user("harshit", "harshit@thebeatles.com", "Harshpassword")
    if request.method == 'POST':
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            print("ENTER INSIDE FORM")
            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password']
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to your home page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
