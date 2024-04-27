from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("================Valid===================================")
            user = form.get_user()
            login(request, user)
            print("====================================================")
            return redirect('upload')  # Redirect to the home page or any other page after login
    else:
        form = AuthenticationForm()
        print(form)
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    print("HERE")
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Saved")
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
