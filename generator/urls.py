from django.urls import path
from .views import *

app_name = 'generator'

urlpatterns = [
            path('', GeneratorHome.as_view(), name='generator-home'),
            path('list', GeneratorList.as_view(), name='generator-list'),
            ]

