from django.urls import path
from .views import *

app_name = 'towersite'

urlpatterns = [
    path('', TowerSiteHome.as_view(), name='tower-site-page'),
    path('search/', TowerSiteResults.as_view(), name='tower-site-results-page'),
]
