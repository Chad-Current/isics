from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', min_length=4, max_length=150, widget=forms.TextInput(attrs={'placeholder':'Minimum of 4 characters'}))
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, help_text='Your password can’t be too similar to your other personal information. \
    Your password must contain at least 8 characters.  \
    Your password can’t be a commonly used password.\
    Your password can’t be entirely numeric.')
    password2 = forms.CharField(label='Re-enter Password', widget=forms.PasswordInput, help_text='Confirm password')
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        c = User.objects.filter(username=username)
        if c.count():
            raise forms.ValidationError('Username already exist')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        domain = email.split('@')[1]
        domain_list = ["dps.state.ia.us","isics.info"]
        if domain not in domain_list:
            raise forms.ValidationError("E-mail already exist or incorrect domain address used")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username'].lower()
        if commit:
            user.save()
        return user
