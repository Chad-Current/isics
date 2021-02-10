from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.core.mail import send_mail, send_mass_mail
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from .models import EmailTo, Sitemaintenance, Email
from .forms import EmailForm, EmailActivationForm
from django.contrib import messages
from django.conf import settings
from datetime import datetime
from dateutil import tz
import pytz

class UserPermissonMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect(settings.LOGIN_URL)
        if not self.has_permission():
            return HttpResponseRedirect('/home')
        return super(UserPermissonMixin, self).dispatch(request, *args, **kwargs)


class EmailHome(UserPermissonMixin, FormView):
    raise_exception = False
    permission_required = 'sitemaintenance.view_sitemaintenance'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = '/'


    template_name = 'sitemaintenance/sitemaintenance_form.html'
    model = Email
    form_class = EmailForm
    success_url  = reverse_lazy('sitemaintenance:site-maintenance-email-listing-page')

    def form_valid(self, form):
        self.subject = form.cleaned_data['subject']
        self.message = form.cleaned_data['message']
        self.tower_cell= form.cleaned_data['tower_cell']
        self.sender = 'ISICS_COMM@Iowa.gov'
        tz = pytz.timezone('US/Central')
        ct = datetime.now(tz=tz).replace(second=0).replace(microsecond=0)
        self.date = ct.strftime('%Y-%m-%d %H:%M:%S')
        site = Sitemaintenance.objects.get(tower_cell=self.tower_cell) #GET ASSOCIATION COUNTY NAMES
        object_list = EmailTo.objects.filter(county__in=site.tower_assoc, is_active=True)# USING tower_assoc to find emailto Personnel
        self.contact_list = []
        try:
            for i in range(len(object_list.values_list())):
                self.contact_list.append(object_list.values_list()[i][3])
            send_mail(self.subject, self.message, self.sender , [*self.contact_list], fail_silently=False)
            Email.objects.create(tower_cell=self.tower_cell, subject=self.subject, message=self.message, sent_list=self.contact_list, date=self.date)
        except TypeError as e:
            print('None value ',e)
        return super().form_valid(form)

class EmailActivation(UserPermissonMixin, UpdateView):
    raise_exception = False
    permission_required = 'sitemaintenance.change_sitemaintenance'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'sitemaintenance/'

    model = EmailTo
    form_class = EmailActivationForm
    template_name = 'sitemaintenance/sitemaintenance_update_email_form.html'
    success_url = reverse_lazy('base:home-page')

class EmailActivationDeletion(UserPermissonMixin, DeleteView):
    raise_exception = False
    permission_required = 'sitemaintenance.change_sitemaintenance'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'sitemaintenance/'

    model = EmailTo
    template_name = 'sitemaintenance/sitemaintenance_delete_email.html'
    success_url = reverse_lazy('base:home-page')


class EmailListing(UserPermissonMixin, ListView):
    raise_exception = False
    permission_required = 'sitemaintenance.view_sitemaintenance'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = '/'

    template_name = 'sitemaintenance/sitemaintenance_list.html'
    model = Email
    context_object_name = 'emails'
    paginate_by = 1
    ordering = ['-date']

    def get_queryset(self):
        return Email.objects.all().order_by('-date')[:10]


class EmailSearch(UserPermissonMixin, ListView):
    raise_exception = False
    permission_required = 'sitemaintenance.view_sitemaintenance'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = '/'

    template_name = 'sitemaintenance/sitemaintenance_email_search.html'
    model = Email
    context_object_name = 'emails'
    paginate_by = 1
    ordering = ['-date']

    def get_queryset(self):
        tower_cell = self.request.GET.get('tower_cell')
        query_start_date = self.request.GET.get('start_date')
        query_end_date = self.request.GET.get('end_date')
        try:
            object_list = Email.objects.filter(Q(tower_cell__istartswith=tower_cell) & Q(time_stamp__gte=query_start_date) & Q(time_stamp__lte=query_end_date)).order_by('-date')[:5]
            if not object_list:
                messages.warning(self.request, 'No Results Found')
            return object_list
        except ValidationError as v:
            print('Null values ',v)
