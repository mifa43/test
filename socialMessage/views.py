from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView, View
from contact.models import AdressEntery
from django.core.mail import send_mail

class SendMessages(ListView):
    model = AdressEntery
    template_name = "main/sendMessage.html"
    fields = ['phoneNumber']
    context_object_name = "obj"

    def get_queryset(self, *args, **kwargs):
        queryset = super(SendMessages, self).get_queryset()
        self.usr = self.request.user
        
        if self.request.GET.get('send') == "Send":               
            message = self.request.GET.get('text')
            email = self.request.GET.get('email')
            
        return queryset
    