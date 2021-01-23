from django import forms
from django.contrib.auth.forms import AuthenticationForm
from user.models import Profile
from sitemaintenance.models import EmailTo
from pointofcontact.models import PointOfContactUpdate

COUNTY_CHOICES = [('Adair', 'Adair'),
 ('Adams', 'Adams'),
 ('Allamakee', 'Allamakee'),
 ('Appanoose', 'Appanoose'),
 ('Audubon', 'Audubon'),
 ('Benton', 'Benton'),
 ('Black Hawk', 'Black Hawk'),
 ('Boone', 'Boone'),
 ('Bremer', 'Bremer'),
 ('Buchanan', 'Buchanan'),
 ('Buena Vista', 'Buena Vista'),
 ('Butler', 'Butler'),
 ('Calhoun', 'Calhoun'),
 ('Carroll', 'Carroll'),
 ('Cass', 'Cass'),
 ('Cedar', 'Cedar'),
 ('Cerro Gordo', 'Cerro Gordo'),
 ('Cherokee', 'Cherokee'),
 ('Chickasaw', 'Chickasaw'),
 ('Clarke', 'Clarke'),
 ('Clay', 'Clay'),
 ('Clayton', 'Clayton'),
 ('Clinton', 'Clinton'),
 ('Crawford', 'Crawford'),
 ('Dallas', 'Dallas'),
 ('Davis', 'Davis'),
 ('Decatur', 'Decatur'),
 ('Delaware', 'Delaware'),
 ('Des Moines', 'Des Moines'),
 ('Dickinson', 'Dickinson'),
 ('Dubuque', 'Dubuque'),
 ('Emmet', 'Emmet'),
 ('Fayette', 'Fayette'),
 ('Floyd', 'Floyd'),
 ('Franklin', 'Franklin'),
 ('Fremont', 'Fremont'),
 ('Greene', 'Greene'),
 ('Grundy', 'Grundy'),
 ('Guthrie', 'Guthrie'),
 ('Hamilton', 'Hamilton'),
 ('Hancock', 'Hancock'),
 ('Hardin', 'Hardin'),
 ('Harrison', 'Harrison'),
 ('Henry', 'Henry'),
 ('Howard', 'Howard'),
 ('Humboldt', 'Humboldt'),
 ('Ida', 'Ida'),
 ('Iowa', 'Iowa'),
 ('Jackson', 'Jackson'),
 ('Jasper', 'Jasper'),
 ('Jefferson', 'Jefferson'),
 ('Johnson', 'Johnson'),
 ('Jones', 'Jones'),
 ('Keokuk', 'Keokuk'),
 ('Kossuth', 'Kossuth'),
 ('Lee', 'Lee'),
 ('Linn', 'Linn'),
 ('Louisa', 'Louisa'),
 ('Lucas', 'Lucas'),
 ('Lyon', 'Lyon'),
 ('Madison', 'Madison'),
 ('Mahaska', 'Mahaska'),
 ('Marion', 'Marion'),
 ('Marshall', 'Marshall'),
 ('Mills', 'Mills'),
 ('Mitchell', 'Mitchell'),
 ('Monona', 'Monona'),
 ('Monroe', 'Monroe'),
 ('Montgomery', 'Montgomery'),
 ('Muscatine', 'Muscatine'),
 ("O'Brien", "O'Brien"),
 ('Osceola', 'Osceola'),
 ('Page', 'Page'),
 ('Palo Alto', 'Palo Alto'),
 ('Plymouth', 'Plymouth'),
 ('Pocahontas', 'Pocahontas'),
 ('Polk', 'Polk'),
 ('Pottawattamie', 'Pottawattamie'),
 ('Poweshiek', 'Poweshiek'),
 ('Ringgold', 'Ringgold'),
 ('Sac', 'Sac'),
 ('Scott', 'Scott'),
 ('Shelby', 'Shelby'),
 ('Sioux', 'Sioux'),
 ('Story', 'Story'),
 ('Tama', 'Tama'),
 ('Taylor', 'Taylor'),
 ('Union', 'Union'),
 ('Van Buren', 'Van Buren'),
 ('Wapello', 'Wapello'),
 ('Warren', 'Warren'),
 ('Washington', 'Washington'),
 ('Wayne', 'Wayne'),
 ('Webster', 'Webster'),
 ('Winnebago', 'Winnebago'),
 ('Winneshiek', 'Winneshiek'),
 ('Woodbury', 'Woodbury'),
 ('Worth', 'Worth'),
 ('Wright', 'Wright')]

#Not used at the moment
class UserForm(AuthenticationForm):
    username = forms.CharField(max_length=255, error_messages={'required':'username required'},\
                                help_text='username must be all lowercase')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class EmailRequestForm(forms.ModelForm):
    county = forms.CharField(widget=forms.Select(choices=COUNTY_CHOICES, attrs={'style':'height:2.5em;width:14em;border-radius:5px;'}))
    class Meta:
        model = EmailTo
        fields = ['name','county','email']


class ContactUpdateForm(forms.ModelForm):
    county = forms.CharField(widget=forms.Select(choices=COUNTY_CHOICES, attrs={'style':'height:2.5em;width:14em;border-radius:5px;'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'style':'height:8em;width:15em;border-radius:5px;'}), required=False)
    organization = forms.CharField(required=True)
    job_title = forms.CharField(required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '555-555-5555'}),required=True)
    cell_or_alternate = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '555-555-5555'}),required=False)
    email = forms.EmailField(required=True)
    class Meta:
        model = PointOfContactUpdate
        fields = '__all__'
