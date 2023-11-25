from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    body = forms.CharField()

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    address = forms.CharField()

class UserUpdateForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Ingrese su mail')
    last_name = forms.CharField(label='Ingrese su Apellido')
    first_name = forms.CharField(label='Ingrese su Nombre')
    address = forms.CharField(label='Ingrese su Direccion')
    img = forms.ImageField(label='Avatar', required=False)
    
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'address', 'img']

class NewProductForm(forms.Form):
    name = forms.CharField()
    category = forms.CharField()
    nationality = forms.CharField()
    price = forms.DecimalField()
    stock = forms.IntegerField()
    img = forms.CharField()
    short_description = forms.CharField()
    description = forms.CharField()