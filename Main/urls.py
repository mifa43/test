"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contact import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contact/', views.contact, name='contact'),
    path('api/person/', views.person, name='person'),
    path('api/addresses/', views.addresses, name='addresses'),
    path('api/list-of-contacts/', views.list_of_contacts, name='list_of_contacts'),
    path('api/list-of-contacts/delete/<int:id>', views.delete, name='delete'),
    path('api/update-contact/<int:id>', views.update_contact, name='update_contact'),
    path('api/add-contact/', views.add_contact, name='add_contact'),
]
