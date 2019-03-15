from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    data = {
        "Followers": [{ "username": "buckyroberts" }, {"username": "llSourcell"}],
        "Following": [{ "username": "buckyroberts" }, {"username": "llSourcell"}]
    }


    if not request.user.is_authenticated:
        return render(request, 'dashboard/landing.html')
    return render(request, 'dashboard/dashboard.html', { "data" : data })

def logout_view(request):
    logout(request)
    return redirect('index')
