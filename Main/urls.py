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
from django.urls import path, include
from django.views.generic import RedirectView
from registration import views as vis
from django.contrib.auth.decorators import login_required
#paths and links in the web application
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path("register/", vis.Register.as_view(), name="register" ),
    path("api/update-contact/<int:pk>", login_required(views.UpdateContact.as_view(), login_url="login"), name="update"),
    path("api/contact-list/delete/<int:pk>", login_required(views.DeleteContact.as_view(), login_url="login"), name="delete"),
    path("api/add-contacts/", login_required(views.AddContacts.as_view(), login_url="login"), name="add-contacts"),
    path("api/contact-list/filter/", login_required(views.FilterContacts.as_view(), login_url="login"), name="Filter"),
    path("api/contact-list/", login_required(views.GetListOfContacts.as_view(), login_url="login"), name="contact-list"),
    path("", login_required(views.Home.as_view(), login_url="login"), name="home"),
    path('admin/', admin.site.urls),
]

# For login_required - if the user is not logged in and tries to access the protected page login_required will reject it and request login