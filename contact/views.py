from django.http import request
from django.shortcuts import redirect, render
from .models import AdressEntery, Person, Contact
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView
from .forms import CreateContact, OptionalForm
from contact import models

# <a href="{% url 'add-contacts' %}">New contact</a>
# <a href="{% url 'contact-list' %}">Contacts</a>       return to nav in base
class Home(ListView):
    model = AdressEntery
    template_name = "main/home.html"
