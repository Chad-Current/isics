from django import forms
from .models import PointOfContact, PointOfContactUpdate


class UpdateContactInfo(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = PointOfContactUpdate
        fields = '__all__'


