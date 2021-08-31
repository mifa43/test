from django.shortcuts import render
from .models import AdressEntery, Person, Contact
from django.views import View

class Home(View):
    def get(self, request):
        return render(request, "main/home.html", {})

class GetListOfContacts(View):
    def get(self, request):
        contact_list = AdressEntery.objects.all()
        counter_for_active = AdressEntery.objects.filter(active=True).count()
        return render(request, "main/contact_list.html", {"contact_list": contact_list, "counter": counter_for_active})

class FilterContacts(View):
    def get(self, request):
        filter = AdressEntery.objects.filter()
        counter_for_active = AdressEntery.objects.filter(active=True).count()
        return render(request, "main/filter.html", {"filter": filter.order_by("-birthDate"), "counter": counter_for_active})