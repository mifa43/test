from django import views
from django.db import reset_queries
from django.http import request
from django.shortcuts import redirect, render
from .models import AdressEntery
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

class Home(ListView):   # this is class and it's return home page
    model = AdressEntery    # model 
    template_name = "main/home.html"        # template

class GetListOfContacts(ListView):  # return all contacts for current user
    model = AdressEntery
    context_object_name = "contact_list" #  this will overwrite variabl in html. on first place is something_list
    template_name = "main/contact_list.html"
    def get_queryset(self) -> list(str): # This method queries the database and filters it
        """
        - Check if the user is active True
            - :True show user
            - :False do not show user
            - :return list of active users
        """
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
    def get_context_data(self, *args, **kwargs):    # the way we use to fill in the values from get_queryset()
        context = super().get_context_data(*args, **kwargs) # when we said super().get_context_data(*args, **kwargs) inherits from get_context_data use ctrl + left click and see where it will take you
        context['counter'] = self.get_queryset().count()    # context['counter'] this is similar to what we used: return render(request, template, {"var": var})
        return context  # and pass to template

class AddContacts(CreateView):
    model = AdressEntery    # db model
    fields = ("name", "gender", "birthDate", "firstName", "lastName", "phoneNumber")    #these are the fields that will be displayed in our form
    template_name = "main/add_contact.html"
    context_object_name = "form" # html variabl form
    success_url = "/api/add-contacts/"  # redirect
    def form_valid(self, form): # this is similar to what we used if form.is_valid() -> bool
        form.instance.user = self.request.user # we assign a user for the field user in model
        return super(AddContacts, self).form_valid(form)    # save form inputs
  
class DeleteContact(DeleteView):    
    model = AdressEntery
    context_object_name = "obj"
    template_name = "main/adressentery_confirm_delete.html"
    success_url = reverse_lazy("contact-list")  # this is redirected to a specific url for the parameter using the name expressed in urls .py   
    def dispatch(self,request, *args, **kwargs):   #this method allows us to use methods such as (post, get, put ..) and allows us to return HTTP methods such as (response, redirect)
        return super(DeleteContact, self).dispatch(request)  #dispatch method will override the second method and allow us to do redirection
        #return redirect('/api/contact-list/')   #render(request, self.template_name, {})
    def get_queryset(self, *args, **kwargs):
        queryset = super(DeleteContact, self).get_queryset()
        queryset.filter(id=self.kwargs['pk'])   # finding a person's id - id is stored in kwargs
        if self.request.GET.get('cancel') == "Cancel":      #we capture the action from the form that the button is pressed              
            print("You have not selected the delete option, so we will take you back to the previous page!") #if it is canceled we return the page back html form action
        elif self.request.GET.get('confirm') == "Confirm":  #if confirm is pressed we display js popup with the message and set the flag active = false
            queryset.filter(id=self.kwargs['pk']).update(active=False)  
        return queryset
    def render_to_response(self, context):  #allows us to use http methods e.g. redirect or response
        if context['object'].active == True:    #contact information is stored in a context variable and we read if active is true
            print("You have not selected the delete option, so we will take you back to the previous page!") #if the flag is active = true it means that the contact has not been deleted and -
            #we are not doing anything because if the chancel button is pressed it automatically returns to the previous page
        elif context['object'].active == False: #if the flag = false we redirect to the list of all contacts
            return redirect('/api/contact-list/')
        return super().render_to_response(context) 
     
class UpdateContact(UpdateView):
    model = AdressEntery
    fields = ("name", "gender", "birthDate", "firstName", "lastName", "phoneNumber")
    context_object_name = "form"
    template_name = "main/update-contact.html"
    success_url = "/api/contact-list/"

class SearchContact(ListView):
    model = AdressEntery
    template_name = "main/search.html"
    context_object_name = "result"
    def get_queryset(self):
        query_input = self.request.GET.get('q') #get form input
        result_obj = AdressEntery.objects.filter(Q(name__icontains=query_input),active=True, user=self.request.user)    #filter user by input, active and user
        #writing SQL queries allows the use of (&), or (|), negation (~) If the operator is not included then by default 'AND' operator is used
        return result_obj
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['counter'] = self.get_queryset().count()    # counting number of contacts in results of search
        return context

#region docs
#1.read more about this dispatch:
# https://docs.djangoproject.com/en/3.2/ref/class-based-views/base/#django.views.generic.base.View.dispatch
# https://stackoverflow.com/questions/47808652/what-is-dispatch-used-for-in-django/47808940
#endregion