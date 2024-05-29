from django.urls import path
from LoginApp import views


app_name = 'LoginApp'

urlpatterns = [
    path('signup/', views.signupView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('profile/', views.user_profileView, name='profile'),    
]