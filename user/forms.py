from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput, help_text='Your password can’t be too similar to your other personal information.\t \
    Your password must contain at least 8 characters.  \
    Your password can’t be a commonly used password.\
    Your password can’t be entirely numeric.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean_email(self):
        data = self.cleaned_data['email'].lower()
        domain = data.split('@')[1]
        domain_list = ["dps.state.ia.us","isics.info"]
        if domain not in domain_list:
            raise forms.ValidationError("Please enter an Email Address with a valid domain")
        return data

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data['username'].lower()
        if commit:
            user.save()
        return user
