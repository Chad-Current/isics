from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView, UpdateView, DeletionMixin, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from sitemaintenance.models import Email, EmailTo
from servicecall.models import ServiceTicket, ServiceTicketArchive
from towersite.models import Site
from ticketsystem.models import SubscriberTicket
from pointofcontact.models import PointOfContactUpdate
from alarm.models import Alarm, AlarmArchive
from notam.models import Notam
from .forms import EmailRequestForm, ContactUpdateForm
import datetime

class UserPermissonMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect(settings.LOGIN_URL)
        if not self.has_permission():
            return HttpResponseRedirect('/home')
        return super(UserPermissonMixin, self).dispatch(request, *args, **kwargs)


class Index(LoginRequiredMixin, ListView):
    template_name = 'base/index.html'
    model = Email

    def get_context_data(self, *args, **kwargs):
        one_year = datetime.datetime.now() - datetime.timedelta(days=1*365)
        self.now = datetime.datetime.now()
        context = super().get_context_data(**kwargs)
        context['emailsent'] = Email.objects.last()
        context['contact'] = PointOfContactUpdate.objects.last()
        context['alarms'] = Alarm.objects.all().order_by('-ticket','-opened')
        context['total_alarms'] = AlarmArchive.objects.filter(Q(time_stamp__gte=one_year)).count() + \
                                         Alarm.objects.filter(Q(timestamp__gte=one_year)).count()
        context['site_trunking'] = Alarm.objects.filter(alarm__icontains='Trunking')
        context['lights'] = Alarm.objects.filter(alarm__icontains='Tower', timestamp__lte=self.now)
        context['ticketsys'] = SubscriberTicket.objects.filter(issue_resolved=False)
        context['ticketsyscount'] = SubscriberTicket.objects.all().count()
        context['email_request'] = EmailTo.objects.filter(is_active=False).last()
        context['notams'] = Notam.objects.all().order_by('date','site_name')
        context['service_tickets'] = ServiceTicket.objects.all().order_by('-date')
        context['total_service_tickets'] = ServiceTicket.objects.filter(Q(date__gte=one_year)).count() + \
                                         ServiceTicketArchive.objects.filter(Q(date__gte=one_year)).count()
        context['towers'] = Site.objects.distinct('site_name','state_owned')
        return context


class SecretIndex(LoginRequiredMixin, ListView):
    template_name = 'base/secret.html'
    model = Email
    
    def get_context_data(self, *args, **kwargs):
        one_year = datetime.datetime.now() - datetime.timedelta(days=1*365)
        self.now = datetime.datetime.now()
        context = super().get_context_data(**kwargs)
        context['emailsent'] = Email.objects.last()
        context['alarms'] = Alarm.objects.all().order_by('-ticket','-opened')
        context['total_alarms'] = AlarmArchive.objects.filter(Q(time_stamp__gte=one_year)).count() + \
                                         Alarm.objects.filter(Q(timestamp__gte=one_year)).count()
        context['lights'] = Alarm.objects.filter(alarm__icontains='Tower', timestamp__lte=self.now)
        context['ticketsys'] = SubscriberTicket.objects.filter(issue_resolved=False)
        context['ticketsyscount'] = SubscriberTicket.objects.all().count()
        context['email_request'] = EmailTo.objects.filter(is_active=False).last()
        context['notams'] = Notam.objects.all().order_by('date','site_name')
        context['service_tickets'] = ServiceTicket.objects.all().order_by('-date')
        context['towers'] = Site.objects.distinct('site_name','state_owned')
        return context


class Visitor(SuccessMessageMixin, FormView):
    template_name = 'base/visitor.html'
    model = EmailTo
    form_class = EmailRequestForm
    success_message = 'Your request has been submitted for review'
    success_url  = reverse_lazy('base:visitor-page')

    def form_valid(self, form):
        self.name = form.cleaned_data['name']
        self.county = form.cleaned_data['county']
        self.email = form.cleaned_data['email']
        try:
            EmailTo.objects.create(name=self.name, county=self.county, email=self.email, is_active=False)
        except TypeError as e:
            print('None value ',e)
        return super().form_valid(form)


class ContactInfo(SuccessMessageMixin, FormView):
    template_name = 'base/updatecontactinfo.html'
    model = PointOfContactUpdate
    form_class = ContactUpdateForm
    success_url = reverse_lazy('base:login')

    def form_valid(self, form):
        self.name = form.cleaned_data['name']
        self.organization = form.cleaned_data['organization']
        self.county = form.cleaned_data['county']
        self.phone = form.cleaned_data['phone']
        self.job_title = form.cleaned_data['job_title']
        self.cell_or_alternate = form.cleaned_data['cell_or_alternate']
        self.email = form.cleaned_data['email']
        self.notes = form.cleaned_data['notes']
        try:
            PointOfContactUpdate.objects.create(name=self.name, \
            organization=self.organization, county=self.county, \
            phone=self.phone, job_title=self.job_title, \
            cell_or_alternate=self.cell_or_alternate, email=self.email, \
            notes=self.notes)
        except TypeError as e:
            print('None value ',e)
        return super().form_valid(form)



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "base/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'your-website-name.com',
					'site_name': 'Website Name',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'https',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("base/password_reset_done")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset_email.html", context={"password_reset_form":password_reset_form})

def error_500(request):
    data = {}
    return render(request, 'base/error_500.html', data)
