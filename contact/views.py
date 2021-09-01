from django.http import request
from django.shortcuts import redirect, render
from .models import AdressEntery, Person, Contact
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView
from .forms import CreateContact, OptionalForm
from contact import models
from django.views.generic.edit import FormView

class Home(ListView):   # this is class and it's return home page
    model = AdressEntery    # model 
    template_name = "main/home.html"        # template

class GetListOfContacts(ListView):
    model = AdressEntery
    context_object_name = "contact_list" #  this will overwrite variabl in html. on first place is something_list
    template_name = "main/contact_list.html"
    def get_queryset(self):
        queryset = super(GetListOfContacts, self).get_queryset()
        return queryset.filter(active=True, user=self.request.user)
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['counter'] = self.get_queryset().count()
        return context

class FilterContacts(ListView):
    model = AdressEntery
    template_name = "main/filter.html"
    context_object_name = "filter"  
    ordering = "-birthDate"     #just like in old version of code ordering == order_by in methods
    def get_queryset(self): # query instance
        queryset = super(FilterContacts, self).get_queryset()   # super used to find the "parent class" and return its object
        return queryset.filter(active=True, user=self.request.user) # return query set as filtrered data
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) # when we said super().get_context_data(*args, **kwargs) inherits from get_context_data use ctrl + left click and see where it will take you
        context['counter'] = self.get_queryset().count()    # context['counter'] this is similar to what we used: return render(request, template, {"var": var})
        return context  # and pass to template

class AddContacts(FormView):
    template_name = "main/add_contact.html"
    form_class = CreateContact  # call form
    context_object_name = "form" # html variabl form
    success_url = "/api/add-contacts/"  # redirect
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

class DeleteContact(ListView):
    template_name = "main/contact_list.html" 
    context_object_name = "contact"
    success_url = "/api/contact-list/"
    def get_queryset(self, *args, **kwargs):
        
        return AdressEntery.objects.filter(id=self.kwargs['pk']).update(active=False)