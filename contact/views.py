from django.shortcuts import redirect, render
from .models import AdressEntery, Person, Contact
from django.views import View
from .forms import CreateContact, OptionalForm
# Added helper class to type and save contact goal is to call views.py in class AddContacts
#region block for helper classes
class Add():
    def __init__(self, name, gender, birth_date, first_name, last_name, phone_number):#params
        self.name = name    #forwarding values and sending to function
        self.gender = gender
        self.birth_date = birth_date
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
    def contact(self):
        add = AdressEntery(name=self.name, gender=self.gender.upper(), birthDate=self.birth_date)
        add.save()  #save contact and create 
        add.person_set.create(firstName=self.first_name, lastName=self.last_name)
        add.contact_set.create(phoneNumber=self.phone_number)
#endregion

class Home(View): #Displaying the home page
    template_name ="main/home.html"
    def get(self, request): # new get method. old method if request.method == 'GET': do_something()
        return render(request, self.template_name, {})

class GetListOfContacts(View):  #Displaying the list of contacts
    template_name = "main/contact_list.html"
    def get(self, request):
        contact_list = AdressEntery.objects.all()   # get all contacts from db
        counter_for_active = AdressEntery.objects.filter(active=True).count()   #count for active contacts
        return render(request, self.template_name, {"contact_list": contact_list, "counter": counter_for_active})

class FilterContacts(View): #Displaying the filtered contact by birth date
    template_name = "main/filter.html"
    def get(self, request):
        filter = AdressEntery.objects.filter()  #filter for parametar is using -birth date with order_by and sort contacts
        counter_for_active = AdressEntery.objects.filter(active=True).count()   #counter
        return render(request, self.template_name, {"filter": filter.order_by("-birthDate"), "counter": counter_for_active})

class AddContacts(View):    #class for adding new contacts
    template_name = "main/add_contact.html"
    form = CreateContact    #form
    def get(self, request): #get form and show in template
        return render(request, self.template_name, {"form": self.form})

    def post(self, request):    #post contact
        form = self.form(request.POST)  #this is new method for request post. old if request.method == 'POST': do_something()
        if form.is_valid(): 
            name, birth_date, first_name, last_name, phone_number = form.cleaned_data['name'], form.cleaned_data['birthDate'], form.cleaned_data['firstName'], form.cleaned_data['lastName'], form.cleaned_data['phoneNumber']
            gender = form.cleaned_data['gender']
            gender = dict(form.fields['gender'].choices)[gender]
            Add(name, gender, birth_date, first_name, last_name, phone_number).contact()    #helper class
            return redirect("http://localhost:8001/api/add-contacts/")  #redirect to same page
        return render(request, self.template_name, {"form": self.form}) 