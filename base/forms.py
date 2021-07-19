from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
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
 ("OBrien", "O'Brien"),
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
    username = forms.CharField(max_length=255, error_messages={'required':'username required'})
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if username != username.lower():
            raise ValidationError('Username must be lower case')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        try:
            username = self.cleaned_data.get('username').lower()
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError('Incorrect password')
            return password
        except AttributeError as a:
            raise ValidationError('and password is incorrect!')
        


class EmailRequestForm(forms.ModelForm):
    county = forms.CharField(widget=forms.Select(choices=COUNTY_CHOICES, attrs={'style':'width:14em;'}))
    class Meta:
        model = EmailTo
        fields = ['name','county','email']


class ContactUpdateForm(forms.ModelForm):
    name = forms.CharField(label='Name *',required=True)
    county = forms.CharField(label='County *',widget=forms.Select(choices=COUNTY_CHOICES))
    notes = forms.CharField(label="Addtional Information", widget=forms.Textarea(attrs={'style':'height:8em;width:61em;border-radius:5px;','placeholder':'Place additional information and multiple county request here.'}), required=False)
    organization = forms.CharField(label='Organization *',required=True)
    job_title = forms.CharField(label='Job title *',required=True)
    phone = forms.CharField(label='Phone *',widget=forms.TextInput(attrs={'placeholder': '555-555-5555'}),required=True)
    cell_or_alternate = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '555-555-5555'}),required=False)
    email = forms.EmailField(label='E-mail *',required=True)
    class Meta:
        model = PointOfContactUpdate
        fields = '__all__'


