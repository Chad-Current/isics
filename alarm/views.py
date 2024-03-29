from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError, DataError
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.template.loader import get_template
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
from xhtml2pdf import pisa
from datetime import datetime
from dateutil.parser import parse
from .models import Alarm, AlarmComment, AlarmArchive
from user.models import Profile
from .forms import AlarmForm, AlarmCommentForm
import pytz



class UserPermissonMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect(settings.LOGIN_URL)
        if not self.has_permission():
            return HttpResponseRedirect('/alarm/')
        return super(UserPermissonMixin, self).dispatch(request, *args, **kwargs)

class AlarmHome(LoginRequiredMixin, TemplateView):
    template_name = 'alarm/alarm_home.html'
    model = Alarm


class AlarmList(LoginRequiredMixin, ListView):
    raise_exception = False
    permission_required = 'alarm.view_alarm'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'alarm/'

    template_name = 'alarm/alarm_list.html'
    model = Alarm
    context_object_name = 'alarms'
    ordering = ['ticket','-timestamp']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()
        context['alarm'] = Alarm.objects.all().order_by('-ticket','timestamp')
        return context


class ArchiveAlarm(UserPermissonMixin, DeleteView):
    raise_exception = False
    permission_required = 'alarm.view_alarmarchive'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'alarm/'

    template_name = 'alarm/alarm_archive.html'
    model = Alarm
    success_url = reverse_lazy('alarm-check:alarm-list')

    def delete(self, *args, **kwargs):
            self.object = self.get_object()
            try:  #AlarmArchive creation here to keep all (single) records of opened and closed alarm (history)
                comments = AlarmComment.objects.filter(original_alarm=self.object.id).values_list('comments', flat=True)
                comments = str(comments).replace("<QuerySet [","")
                comments = str(comments).replace("]>","")
                self.user = self.request.user
                AlarmArchive.objects.create(arcv_site_name=self.object.site, \
                arcv_alarm=self.object.alarm, arcv_alarm_opened=self.object.opened, \
                all_comments=comments, arcv_ticket=self.object.ticket, user_close=self.user)
                
            except IntegrityError as i:
                print('Object creation breaks IntergrityError ', i)
                self.object.delete()
                return render(self.request, template_name='alarm/alarm_home.html')
    

            return super(ArchiveAlarm, self).delete(*args, **kwargs)


class ArchiveAlarmRecords(UserPermissonMixin, ListView):
    raise_exception = False
    permission_required = 'alarm.view_alarmarchive'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'alarm/'

    template_name = 'alarm/alarm_archive_records.html'
    model = AlarmArchive
    context_object_name = 'alarm_archives'
    ordering = ['-time_stamp','arcv_ticket']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alarm_archivces'] = AlarmArchive.objects.all()[:100]
        return context

class AlarmUpdate(UserPermissonMixin, UpdateView):
    raise_exception = False
    permission_required = 'alarm.view_alarm'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'alarm/'

    template_name = 'alarm/alarm_update_form.html'
    model = Alarm
    form_class = AlarmCommentForm
    success_url = reverse_lazy('alarm-check:alarm-list')

    def form_valid(self, form, **kwargs):
        self.comments = form.cleaned_data['comments']
        tz = pytz.timezone('US/Central')
        ct = datetime.now(tz=tz).replace(second=0).replace(microsecond=0)
        self.date = ct.strftime('%Y-%m-%d %H:%M:%S')
        self.user = self.request.user
        try:
            self.object = self.get_object()
            AlarmComment.objects.create(time_stamp=self.date, \
                                        comments=self.comments, \
                                        original_alarm=self.object, \
                                        user_comm=self.user
                                        )
        except TypeError as e:
            print('None value ',e)
        except DataError as d:
            print('Too many characters ',d)
        return super().form_valid(form)


class AlarmDetail(UserPermissonMixin, DetailView):
    raise_exception = False
    permission_required = 'alarm.view_alarm'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'alarm/'

    template_name = 'alarm/alarm_detail.html'
    model = Alarm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alarm_object'] = Alarm.objects.filter(id=self.object.id)
        context['alarm_comment'] = AlarmComment.objects.filter(original_alarm=self.object.id).order_by('-time_stamp')
        return context

class AlarmOpenTicket(UserPermissonMixin, ListView):
        raise_exception = False
        permission_required = 'alarm.view_alarm'
        permisson_denied_message = 'Not authorized to make changes'
        login_url = '/'
        redirect_field_name = 'alarm/'

        template_name = 'alarm/alarm_open.html'
        model = Alarm
        context_object_name = 'alarms'


class AlarmSearch(UserPermissonMixin, ListView):
        raise_exception = False
        permission_required = 'alarm.view_alarm'
        permisson_denied_message = 'Not authorized to make changes'
        login_url = '/'
        redirect_field_name = 'alarm/'

        template_name = 'alarm/alarm_search.html'
        model = Alarm
        context_object_name = 'alarms'

        def get_queryset(self):
            query_site = self.request.GET.get('site')
            query_alarm = self.request.GET.get('alarm')
            start_date = self.request.GET.get('start')
            end_date = self.request.GET.get('end')
            try:
                object_list = Alarm.objects.filter(Q(site__icontains=query_site) & Q(alarm__icontains=query_alarm) \
                                                   & Q(timestamp__gte=start_date) & Q(timestamp__lte=end_date)).order_by('-timestamp','ticket')
                if not object_list:
                    messages.warning(self.request, 'No Results Found')
                return object_list
            except ValidationError as v:
                print('Null values ',v)

class ArchiveAlarmRecords(UserPermissonMixin, ListView):
        raise_exception = False
        permission_required = 'alarm.view_alarmarchive'
        permisson_denied_message = 'Not authorized to make changes'
        login_url = '/'
        redirect_field_name = 'alarm/'

        template_name = 'alarm/alarm_archive_records.html'
        model = AlarmArchive
        queryset = AlarmArchive.objects.order_by('-time_stamp')[:20]
        context_object_name = 'alarm_archives'


class ArchiveAlarmTicket(UserPermissonMixin, TemplateView):
        raise_exception = False
        permission_required = 'alarm.view_alarmarchive'
        permisson_denied_message = 'Not authorized to make changes'
        login_url = '/'
        redirect_field_name = 'alarm/'

        template_name = 'alarm/alarm_archive_ticket.html'
        model = AlarmArchive

class ArchiveAlarmSearchTicket(UserPermissonMixin, ListView):
        raise_exception = False
        permission_required = 'alarm.view_alarmarchive'
        permisson_denied_message = 'Not authorized to make changes'
        login_url = '/'
        redirect_field_name = 'alarm/'

        template_name = 'alarm/alarm_archive_search_ticket.html'
        model = AlarmArchive
        context_object_name = 'alarm_archives'

        def get_queryset(self):
            query_ticket = self.request.GET.get('ticket')
            query_start_date = self.request.GET.get('start_date')
            query_end_date = self.request.GET.get('end_date')
            try:
                object_list = AlarmArchive.objects.filter(Q(arcv_ticket__istartswith=query_ticket) \
                | Q(arcv_ticket__iendswith=query_ticket)\
                & Q(time_stamp__gte=query_start_date)\
                & Q(time_stamp__lte=query_end_date)).order_by('-time_stamp')
                if not object_list:
                    messages.warning(self.request, 'No Results Found')
                return object_list
            except ValidationError as v:
                print('Null values ',v)


class ArchiveAlarmSite(UserPermissonMixin, TemplateView):
        raise_exception = False
        permission_required = 'alarm.view_alarmarchive'
        permisson_denied_message = 'Not authorized to make changes'
        login_url = '/'
        redirect_field_name = 'alarm/'

        template_name = 'alarm/alarm_archive_site.html'
        model = AlarmArchive


class ArchiveAlarmSearchSite(UserPermissonMixin, ListView):
        raise_exception = False
        permission_required = 'alarm.view_alarmarchive'
        permisson_denied_message = 'Not authorized to make changes'
        login_url = '/'
        redirect_field_name = 'alarm/'

        template_name = 'alarm/alarm_archive_search_site.html'
        model = AlarmArchive
        context_object_name = 'alarm_archives'

        def get_queryset(self):
            query_site = self.request.GET.get('site')
            query_start_date = self.request.GET.get('start_date')
            query_end_date = self.request.GET.get('end_date')
            try:
                object_list = AlarmArchive.objects.filter(Q(arcv_site_name__istartswith=query_site) \
                & Q(time_stamp__gte=query_start_date)\
                & Q(time_stamp__lte=query_end_date)).order_by('-time_stamp')
                if not object_list:
                    messages.warning(self.request, 'No Results Found')
                return object_list
            except ValidationError as v:
                print('Null values ',v)


def render_to_pdf(request):
    try:
        object_list = Alarm.objects.all().order_by('-timestamp')
        template_path = 'alarm/openalarmreport.html'
        context = {'open_tickets':object_list}
        context['time'] = datetime.now()
        context['user_request'] = str(request.user.first_name+' '+request.user.last_name)
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="open_tickets_report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
           return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    except AttributeError as a:
        print('User has been logged out, no retrieval of pdf can be performed')
        return redirect('base:login')

