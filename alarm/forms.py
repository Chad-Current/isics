from django import forms
from .models import Alarm, AlarmComment, AlarmArchive

class AlarmForm(forms.ModelForm):
    site_identity = forms.CharField()
    site_name = forms.CharField()
    alarm = forms.CharField()
    alarm_date = forms.CharField()

    class Meta:
        model = Alarm
        exclude = ['time_stamp']
        labels = {
        'site_name':'Site name:',
        'site_id':'Site ID:'}

    def __init__(self, *args, **kwargs):
        super(AlarmForm, self).__init__(*args, **kwargs)
        self.fields['site_identity'].disabled = True
        self.fields['site_name'].disabled = True
        self.fields['alarm'].disabled = True
        self.fields['alarm_date'].disabled = True


class AlarmCommentForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea(attrs={'style':'height:10em;width:25em;border-radius:5px;','placeholder':'Do not copy and paste messages, retype all information'}))

    class Meta:
        model = AlarmComment
        exclude = ['time_stamp', 'original_alarm','user_comm']
    def __init__(self, *args, **kwargs):
        super(AlarmCommentForm, self).__init__(*args, **kwargs)
