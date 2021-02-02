from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Generator


class GeneratorHome(LoginRequiredMixin, ListView):
    model = Generator
    template_name = 'generator/generator.html'
    context_object_name = 'generator_list'
    ordering = ['gen_location']

class GeneratorList(LoginRequiredMixin, ListView):
    model = Generator
    template_name = 'generator/generator_list.html'
    
    def get_queryset(self):
        query_location = self.request.GET.get('location_id')
        try:
            generator_list = Generator.objects.filter(gen_location__icontains=query_location).order_by('gen_location')
            if not generator_list:
                messages.warning(self.request, 'No Results Found')
                return redirect(reverse_lazy(('generator:generator-list')))
            return generator_list
        except ValidationError as v:
            print('Null values ',v)
