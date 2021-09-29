from django import forms
from contact.models import AdressEntery
from django.forms import ModelForm

class AdressForm(ModelForm):
    class Meta:
        model = AdressEntery
        fields = ["phoneNumber"]