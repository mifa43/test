from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView, View
from contact.models import AdressEntery
import webbrowser as web
import time

# Create your views here.
# class Social():

#     def __init__(self, phone, message):
#         self.phone = phone
#         self.message = message
#     def whatsup(self):
#         #num = "+381"+self.phone
        
#         web.open(f"https://web.whatsapp.com/send?phone=+381{self.phone}&text={self.message}")
        
#         time.sleep(5)
       #"https://web.whatsapp.com/send?phone=+3810600977458&text=caooooo"
class SendMessages(ListView):
    model = AdressEntery
    template_name = "main/sendMessage.html"
    fields = ['phoneNumber']
    
    def get_queryset(self, *args, **kwargs):
        queryset = super(SendMessages, self).get_queryset()
        phone = queryset.get(id=self.kwargs['pk'], active=True, user=self.request.user)
        
        if self.request.GET.get('send') == "Send":               
            message = self.request.GET.get('text')
           
        return queryset
    def render_to_response(self, context):
        super().render_to_response(context)
        return redirect("https://web.whatsapp.com/send?phone=+3810600977458&text=caooooo")
         
        # Cao ovo je djangfo contact book whatsup poruka!