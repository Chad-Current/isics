from django.urls import path, include
from .views import *

app_name = 'suggestion'

urlpatterns = [
    path('submit/', NotesView.as_view(), name="notes-page"),
]
