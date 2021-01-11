from django.urls import path
from .views import *
from . import views

app_name = 'ticketsystem'

urlpatterns = [
    path('', TicketSystemHome.as_view(), name='ticket-system-page'),
    path('create/', TicketSystemCreate.as_view(), name='ticket-system-create-page'),
    path('update_radioticket/<int:pk>/', TicketSystemUpdate.as_view(), name='ticket-system-update-page'),
    path('delete_radioticket/<int:pk>/', TicketSystemDelete.as_view(), name='ticket-system-delete-page'),
    path('read/<int:pk>/', TicketSystemRead.as_view(), name='ticket-system-read-page'),
    path('read/?return', TicketSystemReadResults.as_view(), name='ticket-system-read-results-page'),
]
