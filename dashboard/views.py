from django.shortcuts import render, redirect
from django.contrib.auth import logout
from requests import get

github_base_url = "https://api.github.com"

def index(request):

    if not request.user.is_authenticated:
        return render(request, 'dashboard/landing.html')

    followers = get_followers(request.user.username)
    following = get_following(request.user.username)

    data = {
        "Followers": followers,
        "Following": following
    }

    return render(request, 'dashboard/dashboard.html', { "data" : data })

def logout_view(request):
    logout(request)
    return redirect('index')


def get_followers(username):
    url = github_base_url+"/users/{}/followers".format(username)
    data = get(url=url)

    return data.json()

def get_following(username):
    url = github_base_url+"/users/{}/following".format(username)
    data = get(url=url)

    return data.json()
