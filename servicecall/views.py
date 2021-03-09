from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.core.exceptions import ValidationError
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.db.models import Q
from .forms import TicketForm, TicketFormUpdate
from .models import ServiceTicket
from django.conf import settings
from datetime import datetime
from datetime import timedelta
from dateutil import tz
import pytz


class UserPermissonMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated :
            return redirect(settings.LOGIN_URL)
        if not self.has_permission():
            return HttpResponseRedirect('/servicecall/')
        return super(UserPermissonMixin, self).dispatch(request, *args, **kwargs)

class ServiceMap(LoginRequiredMixin, TemplateView):
    template_name = 'servicecall/servicelargemap.html'


class ServiceHome(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'servicecall/service.html'
    models = ServiceTicket
    form_class = TicketForm
    success_message = "Ticket was created successfully"

    def form_valid(self, form):
        self.ticket = form.cleaned_data['ticketno']
        self.site = form.cleaned_data['site_loc']
        self.issue = form.cleaned_data['issue']
        self.subject = str(self.ticket)+' '+str(self.site)
        self.message = str(self.issue)
        tz = pytz.timezone('US/Central')
        ct = datetime.now(tz=tz).replace(second=0).replace(microsecond=0)
        self.date = ct.strftime('%Y-%m-%d %H:%M:%S')
        try:
            ServiceTicket.objects.create(ticketno=self.ticket, site_loc=self.site, issue=self.issue, date=self.date)
            send_mail(self.subject, self.message,'admin@isics.info',['ccurrent@dps.state.ia.us']) 
        except TypeError as e:
            print('None value ',e)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('servicecall:service-call-page')


class ServiceUpdate(UserPermissonMixin, UpdateView):
    raise_exception = False
    permission_required = 'ticketlog.view_ticket'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'servicecall/'

    template_name_suffix = '_update_form'
    model = ServiceTicket
    form_class = TicketFormUpdate
    success_url = reverse_lazy('servicecall:service-list')


class ServiceDelete(UserPermissonMixin, DeleteView):
    raise_exception = False
    permission_required = 'ticketlog.view_ticket'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'servicecall/'

    model = ServiceTicket
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('servicecall:service-list')


class ServiceList(LoginRequiredMixin, ListView):
    template_name = 'servicecall/servicecall_list.html'
    model = ServiceTicket
    context_object_name = 'tickets'
    paginate_by = 2
    ordering = ['-date']


class ServiceSearch(LoginRequiredMixin, ListView):
    model = ServiceTicket
    template_name = 'servicecall/serviceticket_search.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        ticketno = self.request.GET.get('ticket_number')
        query_start_date = self.request.GET.get('start_date')
        query_end_date = self.request.GET.get('end_date')
        try:
            object_list = ServiceTicket.objects.filter(Q(ticketno__istartswith=ticketno) & Q(date__gte=query_start_date) & Q(date__lte=query_end_date)).order_by('date')
            if not object_list:
                messages.warning(self.request, 'No Results Found')
            return object_list
        except ValidationError as v:
            print('Null values ',v)
