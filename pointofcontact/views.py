from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages
from .models import PointOfContact, PointOfContactUpdate
from .forms import UpdateContactInfo


class UserPermissonMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect(settings.LOGIN_URL)
        if not self.has_permission():
            return HttpResponseRedirect('/pointofcontact/')
        return super(UserPermissonMixin, self).dispatch(request, *args, **kwargs)

class PointOfContactHome(LoginRequiredMixin, TemplateView):
        template_name = 'pointofcontact/contactinfo.html'

class PointOfContactViewCounty(LoginRequiredMixin, ListView):
    model = PointOfContact
    template_name = 'pointofcontact/contactinfo.html'
    context_object_name = 'poc'

    def get_queryset(self):
        query = self.request.GET.get('county')
        object_list = PointOfContact.objects.filter(county__istartswith=query).order_by('county')
        if not object_list:
            messages.warning(self.request, 'No Results Found')
        return object_list

class PointOfContactViewName(LoginRequiredMixin, ListView):
    model = PointOfContact
    template_name = 'pointofcontact/contactinfo.html'
    context_object_name = 'poc'

    def get_queryset(self):
        query = self.request.GET.get('name')
        object_list = PointOfContact.objects.filter(Q(name__istartswith=query) | Q(name__iendswith=query)).order_by('name','county')
        if not object_list:
            messages.warning(self.request, 'No Results Found')
        return object_list


class PointOfContactViewTitle(LoginRequiredMixin, ListView):
    model = PointOfContact
    template_name = 'pointofcontact/contactinfo.html'
    context_object_name = 'poc'

    def get_queryset(self):
        query = self.request.GET.get('title')
        object_list = PointOfContact.objects.filter(job_title__icontains=query)
        if not object_list:
            messages.warning(self.request, 'No Results Found')
        return object_list.order_by('county', 'name')


class PointOfContactViewOrganization(LoginRequiredMixin, ListView):
    model = PointOfContact
    template_name = 'pointofcontact/contactinfo.html'
    context_object_name = 'poc'

    def get_queryset(self):
        query = self.request.GET.get('organization')
        object_list = PointOfContact.objects.filter(Q(organization__istartswith=query) | Q(organization__iendswith=query)).order_by('organization','name')
        if not object_list:
            messages.warning(self.request, 'No Results Found')
        return object_list


class PointOfContactViewUpdate(UserPermissonMixin, DeleteView):
    raise_exception = False
    permission_required = 'point_of_contact.change_point_of_contact_update'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = 'pointofcontact/contactinfo.html'
    
    model = PointOfContactUpdate
    form_class = UpdateContactInfo
    context_object_name = 'contactinfo'
    template_name = 'pointofcontact/updatecontact.html'
    success_url = reverse_lazy('home:home-page')


    

