from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views
from .forms import UserForm
app_name = 'base'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='base/login.html',authentication_form=UserForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('home/', Index.as_view(), name='home-page'),
    path('visitor/', Visitor.as_view(), name='visitor-page'),
    path('updatecontactinfo/', ContactInfo.as_view(), name='contact-info-page'),
    path('secret/', IndexSecret.as_view(), name='home-page-secret'),
    path('password_reset', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='base/password/password_reset_done.html'),\
          name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="base/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='base/password/password_reset_complete.html'), \
          name='password_reset_complete'),
    ]
