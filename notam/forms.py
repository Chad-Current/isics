from django import forms
from .models import Notam, NotamExtend

TOWER_CHOICES = [
        ('ADAIR_N', 'ADAIR NORTH'),
        ('ADAMS', 'ADAMS'),
        ('ALBIA', 'ALBIA'),
        ('ALLAMAKEE', 'ALLAMAKEE'),
        ('AMES AREA CELL ', 'AMES AREA CELL '),
        ('APPANOOSE', 'APPANOOSE'),
        ('ATLANTIC', 'ATLANTIC'),
        ('BEAVERDALE', 'BEAVERDALE'),
        ('boone', 'BOONE'),
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
        ('fremont-hamburg', 'FREMONT HAMBURG'),
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
        ('WORTH', 'WORTH'),
        ('WRIGHT', 'WRIGHT'),
        ('ZWINGLE', 'ZWINGLE'),
]

class NotamForm(forms.ModelForm):
        site_name = forms.CharField(widget=forms.Select(choices=TOWER_CHOICES,attrs={'style':'height:3.35em;width:15em;margin-right:2.5em;'}))
        aviation = forms.CharField(label='FAA Number',required=True)
        motorola = forms.CharField(label='Motorola Number',widget=forms.TextInput(attrs={'style':'height:3.3em;width:13em;','placeholder':'If applicable, else N\A'}),required=False)
        notes = forms.CharField(widget=forms.Textarea(attrs={'style':'height:5em;width:43em;'}), required=False)
        class Meta:
            model = Notam
            exclude = ['user', 'date']

        def __init__(self, *args, **kwargs):
            super(NotamForm, self).__init__(*args, **kwargs)

class NotamUpdateForm(forms.ModelForm):
        reason = forms.CharField(label='Explanation for Extension',widget=forms.Textarea(attrs={'style':'height:10em;width:20em;'}),required=True)
        class Meta:
            model = NotamExtend
            fields = ['reason'] 
        
