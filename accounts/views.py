from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        # Check if username taken
        if User.objects.filter(username = username).exists():
            messages.error(request, 'That username is taken by someone, try another')
            return redirect('accounts:register')
        else:
            if User.objects.filter(email = email).exists():
                messages.error(request, 'That email is already used with an account')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username = username, first_name = first_name, last_name= last_name, email = email, password = password)
                user.save()
                messages.success(request, 'Registration successfull, now you can login with your credendials')
                return redirect('accounts:login')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect('attendance:attendance')
        else:
            messages.error(request, 'Username or Password is invalid. Please try again')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, "You'relogged out")
    return redirect('accounts:login')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
