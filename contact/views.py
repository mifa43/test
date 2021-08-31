from django.shortcuts import render
from .models import AdressEntery, Person, Contact
from django.views import View

class Home(View):
    def get(self, request):
        
        return render(request, "main/home.html", {})