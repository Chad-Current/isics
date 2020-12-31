from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import IsicApplicant

#
#
class UserPermissonMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated :
            return redirect(settings.LOGIN_URL)
        if not self.has_permission():
            return HttpResponseRedirect('/home')
        return super(UserPermissonMixin, self).dispatch(request, *args, **kwargs)


class ApplicantHome(UserPermissonMixin, ListView):
    raise_exception = False
    permission_required = 'applicants.view_isics_applicant'
    permisson_denied_message = 'Not authorized to make changes'
    login_url = '/'
    redirect_field_name = '/'


    model = IsicApplicant
    template_name = 'isicsapplicant/member.html'

    context_object_name = 'application'  # Default: object_list
    paginate_by = 10
    queryset = IsicApplicant.objects.all().order_by('applicant')  # Default: Model.objects.all()
