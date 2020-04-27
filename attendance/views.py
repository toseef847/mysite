from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'attendance/index.html')
    else:
        messages.warning(request, 'Please login first')
        return redirect('accounts:login')
