from django.urls import path
from .views import *

app_name = 'servicecall'

urlpatterns = [
    path('', ServiceHome.as_view(), name='service-call-page'),
    path('largemap/', ServiceMap.as_view(), name='service-map'),
    path('update_serviceticket/<int:pk>/', ServiceUpdate.as_view(), name='service-update'),
    path('delete_serviceticket/<int:pk>/', ServiceDelete.as_view(), name='service-delete'),
    path('serviceticket_list/', ServiceList.as_view(), name='service-list'),
    path('serviceticket_search/', ServiceSearch.as_view(), name='service-search'),
    path('serviceticket_archive/', ServiceArchive.as_view(), name='service-archive'),
]
