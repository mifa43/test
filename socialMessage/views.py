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
        usr = self.request.user  #get an email from the currently logged in user
        message = self.request.GET.get('text')  #html input message
        to_email = [self.request.GET.get('email'),] # input target email
        subject = self.request.GET.get('subject')   #email subject/title
        user_password = os.getenv("DJANGO_EMAIL_PASSWORD")#docker env get password
        connection = [usr.email, user_password, False,] #connect to email, if it doesn't work, turn off the settings on the email (less security) and avast
        if self.request.GET.get('send') == "Send":  #pressed button
            send_mail(subject, message, usr.email, to_email, connection)    #send an emal
        return queryset