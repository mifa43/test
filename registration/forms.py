from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
class RegisterForm(UserCreationForm):#the new class contains a reference to the jango register form
    email = forms.EmailField()  #we add a new field

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']    #field display