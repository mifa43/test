from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from .forms import CreateContact, OptionalForm
from .models import AdressEntery, Person, Contact

# Create your views here.
def add_contact(response):
    if response.method == 'POST':
        form = CreateContact(response.POST)     #capturing post requests from the form
        if form.is_valid():     # validate form
            name, birth_date, first_name, last_name, phone_number = form.cleaned_data['name'], form.cleaned_data['birthDate'], form.cleaned_data['firstName'], form.cleaned_data['lastName'], form.cleaned_data['phoneNumber']
            gender = form.cleaned_data['gender']
            gender = dict(form.fields['gender'].choices)[gender]
            #taking values from the form field
            add = AdressEntery(name=name, gender=gender.upper(), birthDate=birth_date)
            add.save()
            add.person_set.create(firstName=first_name, lastName=last_name)
            add.contact_set.create(phoneNumber=phone_number)
            response.user.adressentery.add(add)     # add user to conntact
            #adding a new contact to the table and relation and saving it
        return HttpResponseRedirect("http://localhost:8001/api/add-contact/")   
    else:
        form = CreateContact()  # if not post then just show form 
    return render(response, 'main/add_contact.html', {"form": form})    # rendering template

def list_of_contacts(response):
    if response.method == 'GET':
        for k in response.user.adressentery.all(): #this is how we capture a user who is logged in
            #we filter contacts by logged in user and check if the contact belongs to him
            lista = AdressEntery.objects.filter(user=k.user) 
            for i in AdressEntery.objects.all():    # get all contact from tabel
                #the counter counts contacts by activity and by user
                counter_for_active = AdressEntery.objects.filter(active=True,user=k.user).count()   # counter only active contact
                return render(response, 'main/contact_list.html', {"lista": lista, "i": i, "counter": counter_for_active})  # return lista which is the query variable for html fuction
    return render(response, 'main/contact_list.html', {})   # return template view

def update_contact(response, id):
    if response.method == 'POST':
        form = OptionalForm(response.POST)  #request post from contact update form
        if form.is_valid(): # validate form
            name, birth_date, first_name, last_name, phone_number = form.cleaned_data['name'], form.cleaned_data['birthDate'], form.cleaned_data['firstName'], form.cleaned_data['lastName'], form.cleaned_data['phoneNumber']
            gender = form.cleaned_data['gender']
            gender = dict(form.fields['gender'].choices)[gender]
            if name and gender and birth_date and first_name and last_name and phone_number:    #update only if each field filled
                update = AdressEntery.objects.filter(id=id).update(name=name, gender=gender.upper(), birthDate=birth_date)
                update_rel = AdressEntery.objects.get(id=id)
                update_rel.person_set.update(firstName=first_name, lastName=last_name)
                update_rel.contact_set.update(phoneNumber=phone_number)

            if len(name) >= 1:  # if the value of the name field is equal to and longer than 1 character, enter the value and consider it a request for an update
                update = AdressEntery.objects.filter(id=id).update(name=name)
            else:
                #if not we query the database via id for the current name
                update = AdressEntery.objects.get(id=id)
                update = AdressEntery.objects.filter(id=id).update(name=update.name)
            update = AdressEntery.objects.get(id=id)
            
            if len(update.gender) >= 1: #no solution has been found.. So when changing the male gender is considered the default
                update = AdressEntery.objects.filter(id=id).update(gender=gender.upper())
            # else:
            #     update = AdressEntery.objects.get(id=id)
            #     update = AdressEntery.objects.filter(id=id).update(gender=update.gender.upper())

            if birth_date is not None: # if the value of the birthdate field is is not None, enter the value and consider it a request for an update
                update = AdressEntery.objects.filter(id=id).update(birthDate=birth_date)
            else:   # if not we query the database via id for the current birthdate
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
                
        return HttpResponseRedirect("http://localhost:8001/api/list-of-contacts/")  # redirect and show contact list
    else:
        form = OptionalForm()
        auto = update = AdressEntery.objects.get(id=id)
        person = auto.person_set.get(person_id=id)
        contact = auto.contact_set.get(contact_id=id)
    return render(response, 'main/contact_card.html', {"form": form, "auto": auto, "person": person, "contact": contact})   # rendering card for contact

def delete(response, id): #if the delete link is clicked, the javascript function creates a popup window with a message and a confirmation button
    if id:  #we filter the card id that is selected
        update = AdressEntery.objects.filter(id=id).update(active=False)#if there is, we are disabling contact with that id
        return HttpResponseRedirect("http://localhost:8001/api/list-of-contacts/") 
    #if there is no id we return the contact list
    return HttpResponseRedirect("http://localhost:8001/api/list-of-contacts/")

def filters(response):
    if response.method == "GET":  
        for k in response.user.adressentery.all():  #this is how we capture a user who is logged in
            #we filter contacts by logged in user and check if the contact belongs to him
            f = AdressEntery.objects.filter(user=k.user) #calling the object
            #the counter counts contacts by activity and by user
            counter_for_active = AdressEntery.objects.filter(active=True,user=k.user).count()  #filtering and counting active contacts
            return render(response, 'main/filter.html', {"item": f.order_by('-birthDate'), "check": True, "counter": counter_for_active})
        #if the get method we return the contact list sorted from younger to older
    return render(response, 'main/filter.html', {}) #returning empty contact card

def home(response):
    return render(response, 'main/home.html', {})   #home page for navigation

def redirect(response):
   return HttpResponseRedirect("http://localhost:8001/home")    # if we type localhost:8001/ we want to redirect to home page