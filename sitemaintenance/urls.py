from django.urls import path
from .views import *
from . import views

app_name = 'sitemaintenance'

urlpatterns = [
    path('sitemaintenance/', EmailHome.as_view() , name='site-maintenance-home-page'),
    path('sitemaintenance/emails', EmailListing.as_view(), name='site-maintenance-email-listing-page'),
    path('sitemaintenance/search_emails', EmailSearch.as_view(), name='site-maintenance-email-search-page'),
    path('sitemaintenance/EmailActivation/<int:pk>/', EmailActivation.as_view(), name='site-maintenance-email-activation-page'),
    path('sitemaintenance/EmailActivationDeletion/<int:pk>/', EmailActivationDeletion.as_view(), name='site-maintenance-email-deletion-page'),

]
