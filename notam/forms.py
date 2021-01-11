from django import forms
from .models import Notam

class NotamForm(forms.ModelForm):
    class Meta:
        model = Notam 
        fields = '__all__'
