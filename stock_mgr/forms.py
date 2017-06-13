from django import forms
from django.contrib.auth.models import User
from .models import UserAccount, StoreItem

CHOICES = (('male', 'male',), ('female', 'female',))
choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length = 120, help_text = 'characters.', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Username', 'required': 'required'}))
    first_name = forms.CharField(max_length = 120, help_text = '', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'First Name', 'required': 'required'}))
    last_name = forms.CharField(max_length = 120, help_text = '',  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Surname', 'required': 'required'}))
    email = forms.EmailField(max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'email@example.com', 'required': 'required'}))
    password = forms.CharField(max_length = 15, help_text = '',  widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'password', 'required': 'required'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password',)

class LoginForm(forms.ModelForm):
    email = forms.EmailField(max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'email@example.com', 'required': 'required'}))
    password = forms.CharField(max_length = 15, help_text = '',  widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'password', 'required': 'required'}))
    
    class Meta:
        model = User
        fields = ('email', 'password',)

class UserAccountForm(forms.ModelForm):
    gender              =   forms.ChoiceField( widget=forms.RadioSelect, choices=CHOICES)
    phone_number        = forms.CharField(max_length = 120, help_text = '', widget = forms.NumberInput(attrs = {'class': 'form-control', 'placeholder': 'PhoneNumber', 'required': 'required'}))
    date_of_birth       =   forms.DateField(help_text="", widget=forms.DateInput(attrs= {'class' : 'form-control', 'placeholder' : '1990-03-23', 'required' : 'required'}))
    address             =   forms.CharField(max_length= 120, help_text="", widget=forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Address', 'required' : 'required'}))
    state               =   forms.CharField(max_length= 25, help_text="", widget=forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'State', 'required' : 'required'}))
    country             =   forms.CharField(max_length= 25, help_text="", widget=forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Country', 'required' : 'required'}))
    image               =   forms.FileField(widget=forms.FileInput())
    
    class Meta:
        model = UserAccount
        fields = ( 'gender',  'phone_number', 'date_of_birth', 'address', 'state', 'country', 'image')

class AddItemForm(forms.ModelForm):
    itemName    = forms.CharField(max_length = 120, help_text = 'characters.', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Item Name', 'required': 'required'}))
    itemCode    = forms.CharField(max_length = 120, help_text = '', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Item Code', 'required': 'required'}))
    description = forms.CharField(max_length = 120, help_text = '',  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Item description', 'required': 'required'}))
    quantity    = forms.CharField(max_length = 120,  help_text = 'Numbers',  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'quantity ie.45', 'required': 'required'}))
     

    class Meta:
        model = StoreItem
        fields = ('itemName','itemCode', 'description', 'quantity',)

