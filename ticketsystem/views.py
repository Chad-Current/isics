from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.conf import settings
from datetime import datetime
from dateutil import tz
import pytz
from .forms import TicketForm, TicketUpdateForm, SearchTicketForm
from .models import SubscriberTicket

class UserPermissonMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect(settings.LOGIN_URL)
        if not self.has_permission():
            return HttpResponseRedirect('/tickets/')
        return super(UserPermissonMixin, self).dispatch(request, *args, **kwargs)

class TicketSystemHome(LoginRequiredMixin, ListView):
    template_name = 'ticketsystem/tickets.html'
    model = SubscriberTicket
    context_object_name = 'ticket_list'

class TicketSystemCreate(LoginRequiredMixin, SuccessMessageMixin, FormView):

    form_class = TicketForm
    model = SubscriberTicket
    template_name = 'ticketsystem/tickets_create.html'
    success_message = "Ticket was created successfully"
    success_url = reverse_lazy('ticketsystem:ticket-system-page')

    def form_valid(self, form):
        self.badge_identifier = form.cleaned_data['badge_identifier']
        self.location = form.cleaned_data['location']
        self.talkgroup_assoc = form.cleaned_data['talkgroup_assoc']
        self.rssi = form.cleaned_data['rssi']
        self.mobile = form.cleaned_data['mobile']
        self.portable = form.cleaned_data['portable']
        self.desc_issue = form.cleaned_data['desc_issue']
        self.issue_resolved = form.cleaned_data['issue_resolved']
        self.desc_resolve = form.cleaned_data['desc_resolve']
        tz = pytz.timezone('US/Central')
        ct = datetime.now(tz=tz).replace(second=0).replace(microsecond=0)
        self.date = ct.strftime("%Y-%m-%d %H:%M")
        try:
            SubscriberTicket.objects.create(badge_identifier=self.badge_identifier, location=self.location,\
             talkgroup_assoc=self.talkgroup_assoc, rssi=self.rssi, \
             mobile=self.mobile, portable=self.portable, desc_issue=self.desc_issue, \
             issue_resolved=self.issue_resolved, desc_resolve=self.desc_resolve, \
             date=self.date) # Add sent_list to Emails
        except TypeError as e:
            print('None value ',e)
        return super().form_valid(form)


class TicketSystemUpdate(UserPermissonMixin, UpdateView):
    raise_exception = False
    permission_required = 'tickets.change_ticket'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'tickets/'

    model = SubscriberTicket
    form_class = TicketUpdateForm
    template_name = 'ticketsystem/tickets_update_form.html'
    success_url = reverse_lazy('ticketsystem:ticket-system-read-results-page')


class TicketSystemDelete(UserPermissonMixin, DeleteView):
    raise_exception = False
    permission_required = 'tickets.change_ticket'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'tickets/'

    model = SubscriberTicket
    template_name = 'ticketsystem/tickets_confirm_delete.html'
    success_url = reverse_lazy('ticketsystem:ticket-system-page')

class TicketSystemRead(LoginRequiredMixin, DetailView):
    model = SubscriberTicket
    template_name = 'ticketsystem/ticket_detail.html'
    context_object_name = 'ticket'


class TicketSystemReadResults(LoginRequiredMixin, ListView):
    model = SubscriberTicket
    template_name = 'ticketsystem/tickets_search.html'
    context_object_name = 'tickets'

    def get_queryset(self):

        if self.request.GET.get('badge_identifier'):
            query = self.request.GET.get('badge_identifier')
            object_list = SubscriberTicket.objects.filter(badge_identifier__iexact=query).order_by('-date')
            if not object_list:
                messages.warning(self.request, 'No Results Found')
            return object_list

        elif self.request.GET.get('talkgroup_assoc'):
            query = self.request.GET.get('talkgroup_assoc')
            object_list = SubscriberTicket.objects.filter(talkgroup_assoc__icontains=query).order_by('-date')
            if not object_list:
                messages.warning(self.request, 'No Results Found')
            return object_list

        elif self.request.GET.get('location'):
            query = self.request.GET.get('location')
            object_list = SubscriberTicket.objects.filter(talkgroup_assoc__icontains=query).order_by('-date')
            if not object_list:
                messages.warning(self.request, 'No Results Found')
            return object_list

        elif self.request.GET.get('desc_issue'):
            query = self.request.GET.get('desc_issue')
            object_list = SubscriberTicket.objects.filter(desc_issue__icontains=query).order_by('-date')
            if not object_list:
                messages.warning(self.request, 'No Results Found')
            return object_list

        elif self.request.GET.get('date'):
            query = self.request.GET.get('date')
            object_list = SubscriberTicket.objects.filter(date__istartswith=query).order_by('-date')
            if not object_list:
                messages.warning(self.request, 'No Results Found')
            return object_list
