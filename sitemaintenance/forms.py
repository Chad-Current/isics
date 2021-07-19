from django import forms
from .models import Sitemaintenance, EmailTo, Email

TOWER_CHOICES = [
('ADAIR_N', 'ADAIR NORTH'), #input, display order, check database for accuracy
('ADAMS', 'ADAMS'),
('ALBIA', 'ALBIA'),
('ALLAMAKEE', 'ALLAMAKEE'),
('AMES AREA CELL', 'AMES AREA CELL'),
('APPANOOSE', 'APPANOOSE'),
('ATLANTIC', 'ATLANTIC'),
('BEAVERDALE', 'BEAVERDALE'),
('Boone', 'BOONE'),
('BROOKLYN', 'BROOKLYN'),
('BUCHANAN', 'BUCHANAN'),
('CARROLL', 'CARROLL'),
('CHEROKEE', 'CHEROKEE'),
('CLAYTON', 'CLAYTON'),
('CNCIL BLFFS CELL', 'CNCIL BLFFS CELL'),
('CR CELL', 'CR CELL'),
('dallas ', 'DALLAS '),
('DAVIS ATC', 'DAVIS ATC'),
('DBQ AREA CELL', 'DBQ AREA CELL'),
('DENISON', 'DENISON'),
('DEWITT', 'DEWITT'),
('EMMET', 'EMMET'),
('FAIRFIELD', 'FAIRFIELD'),
('FAYETTE', 'FAYETTE'),
('FRANKLIN', 'FRANKLIN'),
('FREMONT', 'FREMONT'),
('FORT DODGE', 'FORT DODGE'),
('hamilton', 'HAMILTON'),
('HARDIN', 'HARDIN'),
('HARRISON', 'HARRISON'),
('HOOPER', 'HOOPER'),
('humboldt', 'HUMBOLDT'),
('IOWA', 'IOWA'),
('JACKSON', 'JACKSON'),
('JONES', 'JONES'),
('K24IM', 'K24IM'),
('K43LX', 'K43LX'),
('KEOKUK', 'KEOKUK'),
('KOSSUTH', 'KOSSUTH'),
('KTIN', 'KTIN'),
('LEE', 'LEE'),
('LOUISA', 'LOUISA'),
('LOURDES', 'LOURDES'),
('LUCAS', 'LUCAS'),
('MADISON', 'MADISON'),
('MAQUOKETA', 'MAQUOKETA'),
('MARION', 'MARION'),
('MARSHALL', 'MARSHALL'),
('MASON CITY', 'MASON CITY'),
('mills expansion', 'MILLS EXPANSION'),
('MONONA', 'MONONA'),
('montgomery', 'MONTGOMERY'),
('NEWTON', 'NEWTON'),
('OBRIEN', 'OBRIEN'),
('PAGE CELL', 'PAGE CELL'),
('page-bradyville', 'PAGE-BRADYVILLE'),
('PLYMOUTH', 'PLYMOUTH'),
('RINGGOLD', 'RINGGOLD'),
('SCOTT CELL', 'SCOTT CELL'),
('SHELBY', 'SHELBY'),
('SPRINGBROOK', 'SPRINGBROOK'),
('STORM LAKE', 'STORM LAKE'),
('TAMA', 'TAMA'),
('union', 'UNION'),
('VAN WERT', 'VAN WERT'),
('WATERLOO CELL', 'WATERLOO CELL'),
('WESTCOM CELL', 'WESTCOM CELL'),
('WINNEBAGO', 'WINNEBAGO'),
('WOODBURY CELL', 'WOODBURY CELL'),
('worth', 'WORTH'),
('wright', 'WRIGHT'),
('ZWINGLE', 'ZWINGLE'),
('REGION 1', 'REGION 1'),
('REGION 2', 'REGION 2'),
('REGION 3', 'REGION 3'),
('REGION 4', 'REGION 4'),
('REGION 5', 'REGION 5'),
('REGION 6', 'REGION 6'),
('STATE WIDE', 'STATE WIDE'),
]

MAINTENANCE_FIELDS = [
 ('SYSTEM DOWN', 'SYSTEM DOWN'),
 ('SYSTEM TESTING', 'SYSTEM TESTING'),
 ('SITE DOWN', 'SITE DOWN'),
 ('SITE TRUNKING', 'SITE TRUNKING'),
 ('SITE TESTING', 'SITE TESTING'),
]

class EmailForm(forms.Form):
    tower_cell = forms.CharField(widget=forms.Select(choices=TOWER_CHOICES))
    subject = forms.CharField(widget=forms.Select(choices=MAINTENANCE_FIELDS))
    message = forms.CharField(widget=forms.Textarea(attrs={'style':'height:10em;width:20em;'}))

class EmailActivationForm(forms.ModelForm):
    class Meta:
        model = EmailTo
        fields = '__all__'
        labels = {'is_active':'Add to e-mail list?'}

    def __init__(self, *args, **kwargs):
        super(EmailActivationForm, self).__init__(*args, **kwargs)
        self.fields['name'].disabled = True
        self.fields['county'].disabled = True
        self.fields['email'].disabled = True
