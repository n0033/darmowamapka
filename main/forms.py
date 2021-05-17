from django import forms
from phonenumber_field.formfields import PhoneNumberField


class UserForm(forms.Form):
    firstname = forms.CharField(required=True, max_length=20)
    lastname = forms.CharField(required=True, max_length=30)
    email = forms.EmailField(required=True)
    phone_number = PhoneNumberField(required=False)
    checkbox = forms.BooleanField(required=True)
