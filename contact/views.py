from django.http import request
from django.shortcuts import redirect, render
from .models import AdressEntery, Person, Contact
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView
from .forms import CreateContact, OptionalForm
from contact import models
from django.views.generic.edit import FormView

# <a href="{% url 'add-contacts' %}">New contact</a>
#      return to nav in base    <a href="{% url 'Filter' %}">
class Home(ListView):   # this is class and it's return home page
    model = AdressEntery    # model 
    template_name = "main/home.html"        # template

class GetListOfContacts(ListView):
    model = AdressEntery
    template_name = "main/contact_list.html"
    context_object_name = "contact_list" #  this will overwrite variabl in html. on first place is something_list

class FilterContacts(ListView):
    model = AdressEntery
    template_name = "main/filter.html"
    context_object_name = "filter"  
    ordering = "-birthDate"     #just like in old version of code ordering == order_by in methods

class AddContacts(FormView):
    template_name = "main/add_contact.html"
    form_class = CreateContact  # call form
    context_object_name = "form" # html variabl form
    success_url = '/api/add-contacts/'  # redirect

    def post(self, request):
        form = CreateContact(request.POST)  # requesting post method
        if form.is_valid(): # check form fields return true 
            name, birth_date, first_name, last_name, phone_number = form.cleaned_data['name'], form.cleaned_data['birthDate'], form.cleaned_data['firstName'], form.cleaned_data['lastName'], form.cleaned_data['phoneNumber']
            gender = form.cleaned_data['gender']    # get data from form field
            gender = dict(form.fields['gender'].choices)[gender]
            add = AdressEntery(name=name, gender=gender.upper(), birthDate=birth_date)  # add values to db
            add.save()
            add.person_set.create(firstName=first_name, lastName=last_name)
            add.contact_set.create(phoneNumber=phone_number)
            request.user.adressentery.add(add)  # request current loged user
            return redirect("/api/add-contacts/")   # redirect after button presed and its valid form
        return super().post(request)
