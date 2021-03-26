from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from towersite.models import Site


class TowerSiteHome(LoginRequiredMixin, ListView):
    model = Site 
    template_name = 'towersite/tower.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['towers'] = Site.objects.all().order_by('site_id','site_name')
        return context

class TowerSiteResults(LoginRequiredMixin, ListView):
    model = Site
    template_name = 'towersite/tower.html'
    context_object_name = 'tower_list'

    def get_queryset(self):

        if self.request.GET.get('site_name'):
            query = self.request.GET.get('site_name')
            tower_list = Site.objects.filter(site_name__istartswith=query).order_by('site_name', 'state_owned')
            if not tower_list:
                messages.warning(self.request, 'No Results Found')
            return tower_list

        elif self.request.GET.get('site_city'):
            query = self.request.GET.get('site_city')
            tower_list = Site.objects.filter(site_location__icontains=query).order_by('site_name', 'state_owned')
            if not tower_list:
                messages.warning(self.request, 'No Results Found')
            return tower_list

        elif self.request.GET.get('site_id'):
            query = self.request.GET.get('site_id')
            tower_list = Site.objects.filter(site_id__iexact=query).order_by('site_name', 'state_owned')
            if not tower_list:
                messages.warning(self.request, 'No Results Found')
            return tower_list
