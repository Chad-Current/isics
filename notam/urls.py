from django.urls import path
from .views import *

app_name = 'notam'

urlpatterns = [
    path('notam_home/', NotamHome.as_view(), name='notam-home'),
    path('notam_create/', NotamCreate.as_view(), name='notam-create'),
    path('notam_update/<int:pk>/', NotamUpdate.as_view(), name='notam-update'),
    path('notam_detail/<int:pk>/', NotamDetail.as_view(), name='notam-detail'),
    path('notam_delete/<int:pk>/', NotamDelete.as_view(), name='notam-delete'),
    path('notams/?', NotamAll.as_view(), name='notam-all'),
]
