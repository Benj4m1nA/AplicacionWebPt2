from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tarea
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin



class ListaDeTareas(LoginRequiredMixin,ListView):
    model = Tarea  
    context_object_name = 'task'

   

class Descripcion(LoginRequiredMixin,DetailView):
    model = Tarea
    context_object_name = 'task'

class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task')



class EditarTarea(LoginRequiredMixin,UpdateView):
    model = Tarea
    fields = "__all__"
    success_url = reverse_lazy('task')

class Borrar(LoginRequiredMixin,DeleteView):
    model = Tarea
    context_object_name = 'task'
    success_url = reverse_lazy('task')

class CustomLoginView(LoginView):
    template_name = 'Lista/login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('task')