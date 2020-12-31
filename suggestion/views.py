from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Note
from .forms import NoteForm

class NotesView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'suggestion/notes.html'
    model = Note
    form_class = NoteForm
    context_object_name = 'notes'
    success_message = 'Suggestion submitted'
    success_url = reverse_lazy('user:profile-page')

    def form_valid(self, form):
        self.submitted_note = form.cleaned_data['submitted_note']
        try:
            Note.objects.create(submitted_note=self.submitted_note, user_id=self.request.user.id)
        except TypeError as e:
            print('None value ',e)
        return super().form_valid(form)
