from django import forms

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

class NewProductForm(forms.Form):
    name = forms.CharField()
    category = forms.CharField()
    nationality = forms.CharField()
    price = forms.DecimalField()
    stock = forms.IntegerField()
    img = forms.CharField()
    short_description = forms.CharField()
    description = forms.CharField()