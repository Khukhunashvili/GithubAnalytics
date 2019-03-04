from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'dashboard/landing.html')
    return render(request, 'dashboard/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('index')
