from django import views
from django.http import request
from django.shortcuts import redirect, render
from .models import AdressEntery
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

class Home(ListView):   # this is class and it's return home page
    model = AdressEntery    # model 
    template_name = "main/home.html"        # template

class GetListOfContacts(ListView):  # return all contacts for current user
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

class AddContacts(CreateView):
    model = AdressEntery
    fields = ("name", "gender", "birthDate", "firstName", "lastName", "phoneNumber")
    template_name = "main/add_contact.html"
    context_object_name = "form" # html variabl form
    success_url = "/api/add-contacts/"  # redirect
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddContacts, self).form_valid(form)

class DeleteContact(DeleteView):
    model = AdressEntery
    context_object_name = "obj"
    template_name = "main/adressentery_confirm_delete.html"
    success_url = reverse_lazy("contact-list")
   
class UpdateContact(UpdateView):
    model = AdressEntery
    fields = ("name", "gender", "birthDate", "firstName", "lastName", "phoneNumber")
    context_object_name = "form"
    template_name = "main/add_contact.html"
    success_url = "http://localhost:8001/api/contact-list/"

#region docs
#1. allow_empty:
#A boolean specifying whether to display the page if no objects are available. 
#If this is False and no objects are available, the view will raise a 404 instead of displaying an empty page. By default, this is True.

#2.read more about this dispatch:
# https://docs.djangoproject.com/en/3.2/ref/class-based-views/base/#django.views.generic.base.View.dispatch
# https://stackoverflow.com/questions/47808652/what-is-dispatch-used-for-in-django/47808940
#endregion