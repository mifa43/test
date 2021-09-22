from django.contrib.auth.models import User
from django.db import connection
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView
from contact.models import AdressEntery
from django.core.mail import send_mail
import os 
class SendMessages(ListView):
    model = AdressEntery
    template_name = "main/sendMessage.html"
    fields = ['phoneNumber']
    context_object_name = "obj"

    def get_queryset(self, *args, **kwargs):
        queryset = super(SendMessages, self).get_queryset()
        
        
        if self.request.GET.get('send') == "Send":      
            usr = self.request.user              
         
            message = self.request.GET.get('text')
            to_email = [self.request.GET.get('email'),]
            subject = self.request.GET.get('subject')
            user_password = os.getenv("DJANGO_EMAIL_PASSWORD")
            connection = [usr.email, user_password, False,]
            print(subject, message, usr.email, to_email, connection)
            send_mail(subject, message, usr.email, to_email, connection)
        return queryset
    