from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateContact, OptionalForm
from .models import AdressEntery, Person, Contact
# Create your views here.
def add_contact(response):
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

        return HttpResponseRedirect("http://localhost:8001/api/add-contact/")
    else:
        form = CreateContact()
    return render(response, 'main/add_contact.html', {"form": form})

def list_of_contacts(response):
    lista = AdressEntery.objects
    for i in AdressEntery.objects.all():
        counter = AdressEntery.objects.all().count()

        return render(response, 'main/contact_list.html', {"lista": lista, "i": i, "counter": counter})

    return render(response, 'main/contact_list.html', {})


def update_contact(response, id):
    if response.method == 'POST':
        form = OptionalForm(response.POST)
        if form.is_valid():
            name, birth_date, first_name, last_name, phone_number = form.cleaned_data['name'], form.cleaned_data['birthDate'], form.cleaned_data['firstName'], form.cleaned_data['lastName'], form.cleaned_data['phoneNumber']
            gender = form.cleaned_data['gender']
            gender = dict(form.fields['gender'].choices)[gender]
            if name and gender and birth_date and first_name and last_name and phone_number:    #update only if each field filled
                update = AdressEntery.objects.filter(id=id).update(name=name, gender=gender.upper(), birthDate=birth_date)
                update_rel = AdressEntery.objects.get(id=id)
                update_rel.person_set.update(firstName=first_name, lastName=last_name)
                update_rel.contact_set.update(phoneNumber=phone_number)

            if len(name) >= 1:
                update = AdressEntery.objects.filter(id=id).update(name=name)
            else:
                update = AdressEntery.objects.get(id=id)
                update = AdressEntery.objects.filter(id=id).update(name=update.name)
            update = AdressEntery.objects.get(id=id)
            
            if len(update.gender) >= 1:
                update = AdressEntery.objects.filter(id=id).update(gender=gender.upper())
            # else:
            #     update = AdressEntery.objects.get(id=id)
            #     update = AdressEntery.objects.filter(id=id).update(gender=update.gender.upper())

            if birth_date is not None:
                update = AdressEntery.objects.filter(id=id).update(birthDate=birth_date)
            else:
                update = AdressEntery.objects.get(id=id)
                update = AdressEntery.objects.filter(id=id).update(birthDate=update.birthDate)

            if len(first_name) >= 1:
                update = AdressEntery.objects.get(id=id)
                update.person_set.update(firstName=first_name)
            else:
                update = AdressEntery.objects.get(id=id)
                n = update.person_set.get(person_id=id)
                update.person_set.update(firstName=n.firstName)

            if len(last_name) >= 1:
                update = AdressEntery.objects.get(id=id)
                update.person_set.update(lastName=last_name)
            else:
                update = AdressEntery.objects.get(id=id)
                n = update.person_set.get(person_id=id)
                update.person_set.update(lastName=n.lastName)
        
            if phone_number is not None:
                update = AdressEntery.objects.get(id=id)
                update.contact_set.update(phoneNumber=phone_number)
            else:
                update = AdressEntery.objects.get(id=id)
                n = update.contact_set.get(contact_id=id)
                update.contact_set.update(phoneNumber=n.phoneNumber)
                
        print(name,gender, birth_date, first_name, last_name, phone_number)
        return HttpResponseRedirect("http://localhost:8001/api/list-of-contacts/")
    else:
        form = OptionalForm()
    return render(response, 'main/contact_card.html', {"form": form})

def delete(response):
    pass

def contact(response):
    pass

def person(response):
    pass

def addresses(response):
    pass
