from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)  #way of user registration
        #we capture an entry from the form field
        if form.is_valid():
            form.save() #we add to the database
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})