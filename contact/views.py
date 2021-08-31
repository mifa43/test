from django.shortcuts import redirect, render
from .models import AdressEntery, Person, Contact
from django.views import View
from .forms import CreateContact, OptionalForm

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
        
class Add():
    def __init__(self, name, gender, birth_date, first_name, last_name, phone_number):
        self.name = name
        self.gender = gender
        self.birth_date = gender
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def contact(self):
        add = AdressEntery(name=self.name, gender=self.gender.upper(), birthDate=self.birth_date)
        add.save()
        add.person_set.create(firstName=self.first_name, lastName=self.last_name)
        add.contact_set.create(phoneNumber=self.phone_number)

class AddContacts(View):
    template_name = "main/add_contact.html"
    form = CreateContact

    def get(self, request):
        return render(request, self.template_name, {"form": self.form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            all_fields = self.form.declared_fields.keys()
            for i in all_fields:
                s = form.cleaned_data[i]
                print(s)
            form.save()
            return redirect("api/add-contacts/")
        return render(request, self.template_name, {"form": self.form})