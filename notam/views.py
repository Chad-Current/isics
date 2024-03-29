from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.template.loader import get_template
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from datetime import datetime as dt
from .models import Notam, NotamExtend, NotamArchive
from .forms import NotamForm, NotamUpdateForm


class UserPermissonMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect(settings.LOGIN_URL)
        if not self.has_permission():
            return HttpResponseRedirect('/notam/')
        return super(UserPermissonMixin, self).dispatch(request, *args, **kwargs)


class NotamHome(LoginRequiredMixin,TemplateView):
    template_name = 'notam/notam_home.html'

class NotamCreate(UserPermissonMixin, FormView):
    raise_exception = False
    permission_required = 'notam.add_notam'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'notam/'

    form_class = NotamForm
    template_name = 'notam/notam_create.html'
    success_url = reverse_lazy('notam:notam-all')

    def form_valid(self, form):
        self.site_name = form.cleaned_data['site_name']
        self.aviation = form.cleaned_data['aviation']
        self.motorola = form.cleaned_data['motorola']
        self.notes = form.cleaned_data['notes']

        try:
            Notam.objects.create(site_name=self.site_name, date=dt.now(tz=None), aviation=self.aviation, motorola=self.motorola, notes=self.notes, user_id=self.request.user.id)
        except TypeError as e:
            print('None value',e)
        return super().form_valid(form)



class NotamUpdate(UserPermissonMixin,UpdateView):
    raise_exception = False
    permission_required = 'notam.change_notam'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'notam/'

    model = Notam
    form_class = NotamUpdateForm
    template_name = 'notam/notam_update.html'
    success_url = reverse_lazy('notam:notam-all')
    
    def form_valid(self, form):
        self.user = self.request.user
        self.reason = form.cleaned_data['reason']
        self.object = self.get_object()
    
        try:
            NotamExtend.objects.create(reason=self.reason, original_notam_id=self.object.id, user_ex=self.user)
        except TypeError as e:
            print('None value',e)
        return super().form_valid(form)


class NotamDetail(LoginRequiredMixin,DetailView):
    model = Notam
    fields = '__all__'
    template_name = 'notam/notam_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notam_object'] = Notam.objects.filter(id=self.object.id)
        context['notam_extend'] = NotamExtend.objects.filter(original_notam=self.object.id)
        return context

class NotamDelete(UserPermissonMixin,DeleteView):
    raise_exception = False
    permission_required = 'notam.delete_notam'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'notam/'

    model = Notam
    fields = '__all__'
    template_name = 'notam/notam_delete.html'
    context_object_name = 'notam'
    success_url = reverse_lazy('notam:notam-all')


class NotamAll(LoginRequiredMixin,ListView):
    model = Notam
    fields = '__all__'
    template_name = 'notam/notam_list.html'
    context_object_name = 'notams'
    ordering = ['-date']


class NotamArchive(LoginRequiredMixin,ListView):
    model = NotamArchive
    fields = '__all__'
    template_name = 'notam/notam_archive.html'
    context_object_name = 'notams'
    ordering = ['-date']
