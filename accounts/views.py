from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import CustomLoginForm
from django.contrib import messages

def h_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Successfully logged in. Welcome!')
                    return redirect('dashboard')
                else:
                    form.add_error(None, "Username or password is incorrect.")
        else:
            form = CustomLoginForm()
    else:
        return redirect('h_home')
    return render(request, 'home/login.html', {'form': form})

def h_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('h_login')