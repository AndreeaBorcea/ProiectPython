from django import forms
from django.contrib.auth.forms import UserCreationForm

from product.models import ContactRequest, Client


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = '__all__'

class ClientForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'username', 'password1', 'password2']