from django.urls import path
from .views import *

app_name = 'isicsapplicant'

urlpatterns = [
    path('applicant/', ApplicantHome.as_view(), name='applicant-page'),
]
