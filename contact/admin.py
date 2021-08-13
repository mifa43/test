from django.contrib import admin
from .models import AdressEntery, Person, Contact
# Register your models here.
#register your table on admin panel
admin.site.register(AdressEntery) 
admin.site.register(Person) 
admin.site.register(Contact) 