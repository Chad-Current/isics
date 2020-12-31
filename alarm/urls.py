from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'alarm'

urlpatterns = [
    path('', AlarmHome.as_view(), name='alarm-home'),
    path('list/', AlarmList.as_view(), name='alarm-list'),
    path('search/', AlarmSearch.as_view(), name='alarm-search'),
    path('<int:pk>/archive/', ArchiveAlarm.as_view(), name='alarm-archive'),
    path('archive/', ArchiveAlarmRecords.as_view(), name='alarm-archive-records'),
    path('archive/search/', ArchiveAlarmSearch.as_view(), name='alarm-archive-search'),
    path('update/<int:pk>/', AlarmUpdate.as_view(), name='alarm-update'),
    path('detail/<int:pk>/', AlarmDetail.as_view(), name='alarm-detail'),
    path('report/', render_to_pdf, name='alarm-open-tickets'),
    path('report/open/', AlarmOpenTicket.as_view(), name='alarm-open-tickets-page'),
]
