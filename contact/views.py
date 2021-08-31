from django.shortcuts import render
from .models import AdressEntery, Person, Contact
from django.views import View

class Home(View):
    def get(self, request):
        return render(request, "main/home.html", {})

class GetListOfContacts(View):
    def get(self, request):
        contact_list = AdressEntery.objects.all()
        return render(request, "main/contact_list.html", {"contact_list": contact_list})