"""devproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from base import views as base_views
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static

urlpatterns = [
    path(r'session_security/', include('session_security.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='base/password/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='base/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="base/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='base/password/password_reset_complete.html'), name='password_reset_complete'),
    path('', include('base.urls', namespace='home')),
    path('', include('user.urls', namespace='user')),
    path('alarm/', include('alarm.urls', namespace='alarm-check')),
    path('', include('isicsapplicant.urls', namespace='isics-applicant')),
    path('pointofcontact/', include('pointofcontact.urls', namespace='point-of-contant')),
    path('servicecall/', include('servicecall.urls', namespace='service-call')),
    path('tickets/', include('ticketsystem.urls', namespace='ticket-system')),
    path('towersite/', include('towersite.urls', namespace='tower-site')),
    path('', include('sitemaintenance.urls', namespace='site-maintenance')),
    path('', include('suggestion.urls', namespace='suggestion')),
    path('', include('notam.urls', namespace='notam')),
    path('generator/', include('generator.urls', namespace='genertor')),
]

handler500 = base_views.error_500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
