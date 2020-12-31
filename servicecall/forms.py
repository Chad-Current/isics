from django import forms
from django.contrib import messages
from .models import ServiceTicket

SITE_ALIAS = [('Adair North', 'SZ04C9106 ---- Adair North'),
 ('Adair South MW', 'SZ04C91107 ---- Adair South MW'),
 ('Adams', 'SZ04C9103 ---- Adams'),
 ('Albia', 'SZ04C9104 ---- Albia'),
 ('Allamakee', 'SZ04C9105 ---- Allamakee'),
 ('Appanoose', 'SZ04C9107 ---- Appanoose'),
 ('Atlantic', 'SZ04C9153 ---- Atlantic'),
 ('Audubon MW', 'SZ04C91110 ---- Audubon MW'),
 ('Beaverdale', 'SZ04C9111 ---- Beaverdale'),
 ('Benton MW', 'SZ04C91106 ---- Benton MW'),
 ('Blairsburg MW', 'SZ04C91140 ---- Blairsburg MW'),
 ('Bremer', 'SZ04C9112_(GEO) ---- Bremer'),
 ('Brooklyn', 'SZ04C9115 ---- Brooklyn'),
 ('Buchanon', 'SZ04C9116 ---- Buchanon'),
 ('Calhoun MW', 'SZ04C91113 ---- Calhoun MW'),
 ('Carroll', 'SZ04C9118 ---- Carroll'),
 ('Cedar Rapids', 'SZ04C9113 ---- Cedar Rapids'),
 ('Cherokee', 'SZ04C9122 ---- Cherokee'),
 ('Chickasaw MW', 'SZ04C91119 ---- Chickasaw MW'),
 ('Clayton', 'SZ04C9126 ---- Clayton'),
 ('Davis', 'SZ04C9127 ---- Davis'),
 ('Denison', 'SZ04C9128 ---- Denison'),
 ('Dubuque', 'SZ04C9109 ---- Dubuque'),
 ('Emmet', 'SZ04C9130 ---- Emmet'),
 ('Fairfield', 'SZ04C9131 ---- Fairfield'),
 ('Fayette', 'SZ04C9132 ---- Fayette'),
 ('Franklin', 'SZ04C9133 ---- Franklin'),
 ('Fremont', 'SZ04C9134 ---- Fremont'),
 ('Ft Dodge', 'SZ04C9135  ---- Ft Dodge'),
 ('Glenwood', 'SZ04C9110_(GEO) ---- Glenwood'),
 ('Grundy MW', 'SZ04C91138 ---- Grundy MW'),
 ('Hardin', 'SZ04C9140 ---- Hardin'),
 ('Harrison', 'SZ04C9141 ---- Harrison'),
 ('Holy Cross', 'SZ04C9109_(GEO) ---- Holy Cross'),
 ('Hooper', 'SZ04C9144 ---- Hooper'),
 ('Iowa', 'SZ04C9145 ---- Iowa'),
 ('JFHQ Master Site - Zone 1', 'SZ04C91 ---- JFHQ Master Site - Zone 1'),
 ('Jackson', 'SZ04C9146 ---- Jackson'),
 ('Johnson', 'SZ04C911302 ---- Johnson'),
 ('Jones', 'SZ04C9149 ---- Jones'),
 ('K24IM Keosq', 'SZ04C9150 ---- K24IM Keosq'),
 ('K43LX R Rapids', 'SZ04C9151 ---- K43LX R Rapids'),
 ('KIIN DeWitt', 'SZ04C9154 ---- KIIN DeWitt'),
 ('KIIN Ft Dodge', 'SZ04C9156 ---- KIIN Ft Dodge'),
 ('Keokuk', 'SZ04C9152 ---- Keokuk'),
 ('Kossuth', 'SZ04C9155 ---- Kossuth'),
 ('Lee', 'SZ04C9157 ---- Lee'),
 ('Louisa', 'SZ04C9158 ---- Louisa'),
 ('Lourdes', 'SZ04C9159 ---- Lourdes'),
 ('Lucas', 'SZ04C9160 ---- Lucas'),
 ('Lucas Building', 'SZ04C910205 ---- Lucas Building'),
 ('Madison', 'SZ04C9161 ---- Madison'),
 ('Maquoketa', 'SZ04C9162 ---- Maquoketa'),
 ('Marion', 'SZ04C9163 ---- Marion'),
 ('Marshall', 'SZ04C9164 ---- Marshall'),
 ('Mason City', 'SZ04C9165 ---- Mason City'),
 ('Mitchellville MW', 'SZ04C91111 ---- Mitchellville MW'),
 ('Monona', 'SZ04C9167 ---- Monona'),
 ('Muscatine', 'SZ04C9114 ---- Muscatine'),
 ('Newton', 'SZ04C9169 ---- Newton'),
 ('Obrien', 'SZ04C9171 ---- Obrien'),
 ('Page ', 'SZ04C9120 ---- Page '),
 ('Palo Alto MW', 'SZ04C91109 ---- Palo Alto MW'),
 ('Plymouth', 'SZ04C9174 ---- Plymouth'),
 ('Ringgold', 'SZ04C9177 ---- Ringgold'),
 ('Scott', 'SZ04C9114_(GEO) ---- Scott'),
 ('Shelby', 'SZ04C9180 ---- Shelby'),
 ('Sioux MW', 'SZ04C91108 ---- Sioux MW'),
 ('Springbrook', 'SZ04C9182 ---- Springbrook'),
 ('Storm Lake', 'SZ04C9184 ---- Storm Lake'),
 ('Story', 'SZ04C9108_(GEO) ---- Story'),
 ('Tama', 'SZ04C9138 ---- Tama'),
 ('Underwood', 'SZ04C9110 ---- Underwood'),
 ('Van Wert', 'SZ04C9189 ---- Van Wert'),
 ('Waterloo', 'SZ04C9112 ---- Waterloo'),
 ('Winnebago', 'SZ04C9192 ---- Winnebago'),
 ('Woodward', 'SZ04C9108 ---- Woodward'),
 ('Zwingle', 'SZ04C9196 ---- Zwingle')]


class TicketForm(forms.ModelForm):
    ticketno = forms.CharField(label='Ticket #')
    site_loc = forms.CharField(label='Site',widget=forms.Select(choices=SITE_ALIAS))
    issue = forms.CharField(label='Issue',widget=forms.Textarea(attrs={'style':'height:10em;width:16em;border-radius:5px;'}))

    class Meta:
        model = ServiceTicket
        exclude = ['date']

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        # self.fields['site_identity'].disabled = True
        # self.fields['site_name'].disabled = True
        # self.fields['alarm'].disabled = True
        # self.fields['alarm_date'].disabled = True
