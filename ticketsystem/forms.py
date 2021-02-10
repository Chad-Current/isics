from django import forms
from .models import SubscriberTicket

TALKGROUP_CHOICES = [('DPS CALL 1-A', 'DPS CALL 1-A'),
 ('DPS LAW 2-A', 'DPS LAW 2-A'),
 ('DPS LAW 3-A', 'DPS LAW 3-A'),
 ('DPS LAW 4-A', 'DPS LAW 4-A'),
 ('DPS LAW 5-A', 'DPS LAW 5-A'),
 ('TAC 6-A', 'TAC 6-A'),
 ('TAC 7-A', 'TAC 7-A'),
 ('TAC 8-A', 'TAC 8-A'),
 ('TAC 9-A', 'TAC 9-A'),
 ('ETAC 10-A', 'ETAC 10-A'),
 ('ETAC 11-A', 'ETAC 11-A'),
 ('GTAC 12-A', 'GTAC 12-A'),
 ('P16 CALL 13-A', 'P16 CALL 13-A'),
 ('EMERGENCY A', 'EMERGENCY A'),
 ('AREA A ALL', 'AREA A ALL'),
 ('EXTAC-5', 'EXTAC-5'),
 ('EXTAC-6', 'EXTAC-6'),
 ('EXTAC-7', 'EXTAC-7'),
 ('EXTAC-8', 'EXTAC-8'),
 ('EXTAC-9', 'EXTAC-9'),
 ('E-NTAC2A', 'E-NTAC2A'),
 ('E-NTAC3A', 'E-NTAC3A'),
 ('E-NTAC4A', 'E-NTAC4A'),
 ('E-CTAC5A', 'E-CTAC5A'),
 ('E-CTAC6A', 'E-CTAC6A'),
 ('E-CTAC7A', 'E-CTAC7A'),
 ('DPS CALL 1-B', 'DPS CALL 1-B'),
 ('DPS LAW 2-B', 'DPS LAW 2-B'),
 ('DPS LAW 3-B', 'DPS LAW 3-B'),
 ('DPS LAW 4-B', 'DPS LAW 4-B'),
 ('DPS LAW 5-B', 'DPS LAW 5-B'),
 ('TAC 6-B', 'TAC 6-B'),
 ('TAC 7-B', 'TAC 7-B'),
 ('TAC 8-B', 'TAC 8-B'),
 ('TAC 9-B', 'TAC 9-B'),
 ('ETAC 10-B', 'ETAC 10-B'),
 ('ETAC 11-B', 'ETAC 11-B'),
 ('GTAC 12-B', 'GTAC 12-B'),
 ('GTAC 13-B', 'GTAC 13-B'),
 ('EMERGENCY B', 'EMERGENCY B'),
 ('AREA B ALL', 'AREA B ALL'),
 ('E-NTAC2B', 'E-NTAC2B'),
 ('E-NTAC3B', 'E-NTAC3B'),
 ('E-NTAC4B', 'E-NTAC4B'),
 ('E-CTAC5B', 'E-CTAC5B'),
 ('E-CTAC6B', 'E-CTAC6B'),
 ('E-CTAC7B', 'E-CTAC7B'),
 ('DPS CALL 1-C', 'DPS CALL 1-C'),
 ('DPS LAW 2-C', 'DPS LAW 2-C'),
 ('DPS LAW 3-C', 'DPS LAW 3-C'),
 ('DPS LAW 4-C', 'DPS LAW 4-C'),
 ('DPS LAW 5-C', 'DPS LAW 5-C'),
 ('TAC 6-C', 'TAC 6-C'),
 ('TAC 7-C', 'TAC 7-C'),
 ('TAC 8-C', 'TAC 8-C'),
 ('TAC 9-C', 'TAC 9-C'),
 ('ETAC 10-C', 'ETAC 10-C'),
 ('ETAC 11-C', 'ETAC 11-C'),
 ('GTAC 12-C', 'GTAC 12-C'),
 ('GTAC 13-C', 'GTAC 13-C'),
 ('EMERGENCY C', 'EMERGENCY C'),
 ('AREA C ALL', 'AREA C ALL'),
 ('E-NTAC2C', 'E-NTAC2C'),
 ('E-NTAC3C', 'E-NTAC3C'),
 ('E-NTAC4C', 'E-NTAC4C'),
 ('E-CTAC5C', 'E-CTAC5C'),
 ('E-CTAC6C', 'E-CTAC6C'),
 ('E-CTAC7C', 'E-CTAC7C'),
 ('DPS CALL 1-D', 'DPS CALL 1-D'),
 ('DPS LAW 2-D', 'DPS LAW 2-D'),
 ('DPS LAW 3-D', 'DPS LAW 3-D'),
 ('DPS LAW 4-D', 'DPS LAW 4-D'),
 ('DPS LAW 5-D', 'DPS LAW 5-D'),
 ('TAC 6-D', 'TAC 6-D'),
 ('TAC 7-D', 'TAC 7-D'),
 ('TAC 8-D', 'TAC 8-D'),
 ('TAC 9-D', 'TAC 9-D'),
 ('ETAC 10-D', 'ETAC 10-D'),
 ('ETAC 11-D', 'ETAC 11-D'),
 ('GTAC 12-D', 'GTAC 12-D'),
 ('GTAC 13-D', 'GTAC 13-D'),
 ('EMERGENCY D', 'EMERGENCY D'),
 ('AREA D ALL', 'AREA D ALL'),
 ('E-NTAC2D', 'E-NTAC2D'),
 ('E-NTAC3D', 'E-NTAC3D'),
 ('E-NTAC4D', 'E-NTAC4D'),
 ('E-CTAC5D', 'E-CTAC5D'),
 ('E-CTAC6D', 'E-CTAC6D'),
 ('E-CTAC7D', 'E-CTAC7D'),
 ('CENTRAL IOWA', 'CENTRAL IOWA'),
 ('DUBUQUE DTF', 'DUBUQUE DTF'),
 ('DMPD NARC', 'DMPD NARC'),
 ('JOHNSON TF', 'JOHNSON TF'),
 ('LEE-SEIN', 'LEE-SEIN'),
 ('MID IOWA TF', 'MID IOWA TF'),
 ('MINE TF', 'MINE TF'),
 ('MUSCATINE', 'MUSCATINE'),
 ('NORTHCENTRAL', 'NORTHCENTRAL'),
 ('IOWA DNE', 'IOWA DNE'),
 ('SCOTT TF', 'SCOTT TF'),
 ('SOUTHCENTRAL', 'SOUTHCENTRAL'),
 ('SE IOWA TF', 'SE IOWA TF'),
 ('SWINE TF', 'SWINE TF'),
 ('TRI-COUNTY TF', 'TRI-COUNTY TF'),
 ('TRI-STATE TF', 'TRI-STATE TF')]

class TicketForm(forms.ModelForm):
    badge_identifier = forms.IntegerField()
    location = forms.CharField(widget=forms.TextInput())
    talkgroup_assoc = forms.CharField(widget=forms.Select(choices=TALKGROUP_CHOICES,attrs={'style':'height:3em;width:14em;border-radius:5px;'}))
    rssi = forms.IntegerField()
    mobile = forms.BooleanField(required=False)
    portable = forms.BooleanField(required=False)
    desc_issue = forms.CharField(widget=forms.Textarea(attrs={'style':'height:5em;width:15em;border-radius:5px;'}))
    issue_resolved = forms.BooleanField(required=False)
    desc_resolve = forms.CharField(widget=forms.Textarea(attrs={'style':'height:5em;width:15em;border-radius:5px;'}), required=False)

    class Meta:
        model = SubscriberTicket
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)


class TicketUpdateForm(forms.ModelForm):
    badge_identifier = forms.IntegerField()
    location = forms.CharField(widget=forms.TextInput())
    talkgroup_assoc = forms.CharField(widget=forms.Select(choices=TALKGROUP_CHOICES))
    rssi = forms.IntegerField()
    mobile = forms.BooleanField(required=False)
    portable = forms.BooleanField(required=False)
    desc_issue = forms.CharField(widget=forms.Textarea(attrs={'style':'height:10em;width:20em;border-radius:5px;'}))
    issue_resolved = forms.BooleanField(required=False)
    desc_resolve = forms.CharField(widget=forms.Textarea(attrs={'style':'height:10em;width:20em;border-radius:5px;'}), required=False)

    class Meta:
        model = SubscriberTicket
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TicketUpdateForm, self).__init__(*args, **kwargs)
        self.fields['badge_identifier'].disabled = True
        self.fields['location'].disabled = True
        self.fields['talkgroup_assoc'].disabled = True
        self.fields['mobile'].disabled = True
        self.fields['portable'].disabled = True
        self.fields['rssi'].disabled = True
        self.fields['desc_issue'].disabled = True


class SearchTicketForm(forms.Form):
    badge_identifier = forms.IntegerField()
    location = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    talkgroup_assoc = forms.CharField()
    #Date look up Possibly
