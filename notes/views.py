from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from contact.models import AdressEntery
# Create your views here.

class ToDoList(ListView):
    model = AdressEntery
    template_name = "main/note.html"