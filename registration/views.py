from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Register(CreateView):
    form_class = RegisterForm
    #context_object_name = "form"
    template_name = "register/register.html"
    success_url = reverse_lazy("home")
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(Register, self).form_valid(form)
# def register(response):
#     if response.method == 'POST':
#         form = RegisterForm(response.POST)  #way of user registration
#         #we capture an entry from the form field
#         if form.is_valid():
#             form.save() #we add to the database
#     else:
#         form = RegisterForm()

#     return render(response, "register/register.html", {"form": form})