from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from user.views import *

app_name = 'user'

urlpatterns = [
    path('register/', Signup.as_view(), name="register"),
    path('sent/', ActivationSent.as_view(), name="activation-sent"),
    path('activate/<slug:uidb64>/<slug:token>/', Activate.as_view(),name='activate'),
    path('user/', UserAccount.as_view() , name='profile-page'),
]
