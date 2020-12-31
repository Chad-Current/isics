from django import forms
from .models import Note

class NoteForm(forms.Form):
    submitted_note = forms.CharField(widget=forms.Textarea(attrs={'size':'40'}))
