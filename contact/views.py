from django.shortcuts import render
from .models import AdressEntery, Person, Contact
from django.views import View

class Home(View):
    template_name ="main/home.html"

    def get(self, request):
        return render(request, self.template_name, {})

class GetListOfContacts(View):
    template_name = "main/contact_list.html"

    def get(self, request):
        contact_list = AdressEntery.objects.all()
        counter_for_active = AdressEntery.objects.filter(active=True).count()
        return render(request, self.template_name, {"contact_list": contact_list, "counter": counter_for_active})

class FilterContacts(View):
    template_name = "main/filter.html"

    def get(self, request):
        filter = AdressEntery.objects.filter()
        counter_for_active = AdressEntery.objects.filter(active=True).count()
        return render(request, self.template_name, {"filter": filter.order_by("-birthDate"), "counter": counter_for_active})
