from typing import Counter
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateContact
from .models import AdressEntery, Person, Contact

# Create your views here.
def add_contact(response):
    #This endpoint enters the contact information in our table
    if response.method == 'POST':
        form = CreateContact(response.POST)
        if form.is_valid():
            name, birth_date, first_name, last_name, phone_number = form.cleaned_data['name'], form.cleaned_data['birthDate'], form.cleaned_data['firstName'], form.cleaned_data['lastName'], form.cleaned_data['phoneNumber']
            gender = form.cleaned_data['gender']
            gender = dict(form.fields['gender'].choices)[gender]

            add = AdressEntery(name=name, gender=gender.upper(), birthDate=birth_date)
            add.save()
            add.person_set.create(firstName=first_name, lastName=last_name)
            add.contact_set.create(phoneNumber=phone_number)

        return HttpResponseRedirect("http://localhost:8001/api/add-contact/")   #if the form is valid, we redirect to the same page with the restarted fields   
    else:
        form = CreateContact()
    return render(response, 'main/add_contact.html', {"form": form})

def list_of_contacts(response):
    lista = AdressEntery.objects
    for i in AdressEntery.objects.all():
        counter = AdressEntery.objects.all().count()
        
        return render(response, 'main/contact_list.html', {"lista": lista, "i": i, "counter": counter})

    return render(response, 'main/contact_list.html', {})


def update_contact(response):
    pass

def delete(response):
    pass

def contact(response):
    pass

def person(response):
    pass

def addresses(response):
    pass
