from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages
from .models import PointOfContact



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
#            return render(self.request, template_name='pointofcontact/contactinfo.html')
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
#            return render(self.request, template_name='pointofcontact/contactinfo.html')
        return object_list

class PointOfContactViewOrganization(LoginRequiredMixin, ListView):
    model = PointOfContact
    template_name = 'pointofcontact/contactinfo.html'
    context_object_name = 'poc'

    def get_queryset(self):
        query = self.request.GET.get('organization')
        object_list = PointOfContact.objects.filter(Q(organization__istartswith=query) | Q(organization__iendswith=query)).order_by('organization','name')
        if not object_list:
            messages.warning(self.request, 'No Results Found')
#            return render(self.request, template_name='pointofcontact/contactinfo.html')
        return object_list

class PointOfContactViewLevel(LoginRequiredMixin, ListView):
    model = PointOfContact
    template_name = 'pointofcontact/contactinfo.html'
    context_object_name = 'poc'

    def get_queryset(self):
        query = self.request.GET.get('level')
        object_list = PointOfContact.objects.filter(user_lvl__iexact=query)
        if not object_list:
            messages.warning(self.request, 'No Results Found')
 #           return render(self.request, template_name='pointofcontact/contactinfo.html')
        return object_list.order_by('county', 'name')
