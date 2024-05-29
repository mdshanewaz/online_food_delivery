from django.urls import path
from SubscriptionApp import views


app_name = 'SubscriptionApp'

urlpatterns = [
    path('', views.homeView, name='home'),
    path('basic/', views.basicPakView, name='basic'),
    path('premium/', views.perimumPakView, name='premium'),
]