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
from contact import views
from django.conf.urls import url
from django.urls import path

#paths and links in the web application
urlpatterns = [
    # path("api/add-contacts/", views.AddContacts.as_view(), name="add-contacts"),
    # path("api/contact-list/filter/", views.FilterContacts.as_view(), name="Filter"),
    # path("api/contact-list/", views.GetListOfContacts.as_view(), name="contact-list"),
    path("", views.Home.as_view(), name="home"),
    path('admin/', admin.site.urls),
]