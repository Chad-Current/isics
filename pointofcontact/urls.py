from django.urls import path
from .views import *

app_name = 'pointofcontact'

urlpatterns = [
    path('pointofcontact/', PointOfContactHome.as_view(), name='point-of-contact-page'),
    path('pointofcontact/?county', PointOfContactViewCounty.as_view(), name='point-of-contact-county-results'),
    path('pointofcontact/?name', PointOfContactViewName.as_view(), name='point-of-contact-name-results'),
    path('pointofcontact/?organization', PointOfContactViewOrganization.as_view(), name='point-of-contact-organization-results'),
    path('pointofcontact/?level', PointOfContactViewLevel.as_view(), name='point-of-contact-level-results'),
]
