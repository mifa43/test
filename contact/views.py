from django.http import request
from django.shortcuts import redirect, render
from .models import AdressEntery, Person, Contact
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView
from .forms import CreateContact, OptionalForm
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
    model = AdressEntery
    allow_empty = False
    template_name = "main/contact_list.html" 
    context_object_name = "contact"
    def get_queryset(self, *args, **kwargs):
        queryset = super(DeleteContact, self).get_queryset()
        return queryset.filter(id=self.kwargs['pk']).update(active=False)   # filter by clicked contact card get id and set active false
    def dispatch(self,request, *args, **kwargs):   #this method allows us to use methods such as (post, get, put ..) and allows us to return HTTP methods such as (response, redirect)
        super(DeleteContact, self).dispatch(request)  #dispatch method will override the second method and allow us to do redirection
        return redirect('/api/contact-list/')

class UpdateContact(UpdateView):
    model = AdressEntery
    #fields = ("name", "gender", "birthDate")
    context_object_name = "auto"
    template_name = "main/contact_card.html"
    def get(self, request,*args,**kwargs):
        a  = AdressEntery.objects.get(id=self.kwargs['pk'])
        person = a.person_set.get(person_id=self.kwargs['pk'])
        contact = a.contact_set.get(contact_id=self.kwargs['pk'])
        return render(request, self.template_name, {"a": a,"person": person, "contact": contact})

#region docs
#1. allow_empty:
#A boolean specifying whether to display the page if no objects are available. 
#If this is False and no objects are available, the view will raise a 404 instead of displaying an empty page. By default, this is True.

#2.read more about this dispatch:
# https://docs.djangoproject.com/en/3.2/ref/class-based-views/base/#django.views.generic.base.View.dispatch
# https://stackoverflow.com/questions/47808652/what-is-dispatch-used-for-in-django/47808940
#endregion