from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import RegisterForm
from django.urls import reverse_lazy

# Create your views here.

class Register(CreateView):
    """
    For registration we use the fields from the registration form
    """
    form_class = RegisterForm
    template_name = "register/register.html"
    success_url = reverse_lazy("home")