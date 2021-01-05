from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .tokens import account_activation_token
from .models import Profile
from .forms import SignUpForm
from .tokens import account_activation_token



class UserAccount(LoginRequiredMixin, TemplateView):
    template_name = 'user/useraccount.html'
    model = User
    context_object_name = 'profile'

class ActivationSent(TemplateView):
    template_name = 'user/activation_sent.html'


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home:home-page')
    else:
        return render(request, 'user/activation_invalid.html')

def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name').capitalize()
            user.profile.last_name = form.cleaned_data.get('last_name').capitalize()
            user.profile.email = form.cleaned_data.get('email').lower()
            user.profile.username = form.cleaned_data.get('username').lower()
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template()
            # and calls its render() method immediately.
            message = render_to_string('user/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('user:activation-sent')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})
