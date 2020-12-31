from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Site


class TowerSiteHome(LoginRequiredMixin, TemplateView):
    template_name = 'towersite/tower.html'

class TowerSiteResults(LoginRequiredMixin, ListView):
    model = Site
    template_name = 'towersite/tower.html'

    def get_queryset(self):

        if self.request.GET.get('site_name'):
            query = self.request.GET.get('site_name')
            object_list = Site.objects.filter(site_name__istartswith=query).order_by('site_name', 'state_owned')
            if not object_list:
                messages.warning(self.request, 'No Results Found')
            return object_list

        elif self.request.GET.get('site_id'):
            query = self.request.GET.get('site_id')
            object_list = Site.objects.filter(site_id__iexact=query).order_by('site_name', 'state_owned')
            if not object_list:
                messages.warning(self.request, 'No Results Found')
            return object_list
