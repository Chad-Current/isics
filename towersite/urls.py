from django.urls import path
from .views import *

app_name = 'towersite'

urlpatterns = [
    path('towersite/', TowerSiteHome.as_view(), name='tower-site-page'),
    path('towersite/?sitename', TowerSiteResults.as_view(), name='tower-site-results-page'),
]
