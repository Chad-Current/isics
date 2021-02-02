from django.urls import path
from .views import *

app_name = 'pointofcontact'

urlpatterns = [
    path('', PointOfContactHome.as_view(), name='point-of-contact-page'),
    path('county/', PointOfContactViewCounty.as_view(), name='point-of-contact-county-results'),
    path('name/', PointOfContactViewName.as_view(), name='point-of-contact-name-results'),
    path('organization/', PointOfContactViewOrganization.as_view(), name='point-of-contact-organization-results'),
    path('level/', PointOfContactViewLevel.as_view(), name='point-of-contact-level-results'),
]
