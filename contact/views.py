from django.shortcuts import render
from .models import AdressEntery, Person, Contact
from django.views import View

class Home(View):
    def get(self, request):
        contact = AdressEntery.objects.all()
        return render(request, "main/home.html", {"contact": contact})