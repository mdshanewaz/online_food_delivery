from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from SubscriptionApp.models import PackageModel
from SubscriptionApp.forms import PackageForm

from django.contrib.auth.decorators import login_required

# Create your views here.


def homeView(request):
    title = 'FOODIES'
    return render(request, 'SubscriptionApp/home.html', context={"title":title})


@login_required
def basicPakView(request):
    title = 'BASIC'
    form = PackageForm
    
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            package = form.save(commit=False)
            package.user = request.user
            package.title = 'Basic'
            form.save()
            #messages.success(request, "Account Created Successfully!")
            return HttpResponseRedirect(reverse('LoginApp:profile'))
    return render(request, 'SubscriptionApp/package.html', context={'title':title, 'form':form})


@login_required
def perimumPakView(request):
    title = 'PREMIUM'
    return render(request, 'SubscriptionApp/package.html', context={'title':title})