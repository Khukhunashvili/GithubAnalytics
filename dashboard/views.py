from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    return render(request, 'dashboard/landing.html')


def logout_view(request):
    logout(request)
    return redirect('index')
