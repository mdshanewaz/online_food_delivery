from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.


def homeView(request):
    title = 'FOODIES'
    return render(request, 'SubscriptionApp/home.html', context={"title":title})


def basicPakView(request):
    title = 'BASIC'
    return render(request, 'SubscriptionApp/package.html', context={'title':title})


def perimumPakView(request):
    title = 'PREMIUM'
    return render(request, 'SubscriptionApp/package.html', context={'title':title})