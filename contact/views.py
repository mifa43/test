from django.http import request
from django.shortcuts import redirect, render
from .models import AdressEntery, Person, Contact
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView
from .forms import CreateContact, OptionalForm
from contact import models

# <a href="{% url 'add-contacts' %}">New contact</a>
#      return to nav in base    <a href="{% url 'Filter' %}">
class Home(ListView):   # this is class and it's return home page
    model = AdressEntery    # model 
    template_name = "main/home.html"        # template

class GetListOfContacts(ListView):
    model = AdressEntery
    template_name = "main/contact_list.html"
    context_object_name = "contact_list" #  this will overwrite variabl in html. on first place is something_list