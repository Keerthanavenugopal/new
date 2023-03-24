from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import photo,team
# Create your views here.

def home(request):
    return render(request,'index.html')
def demo(request):
    obj = photo.objects.all()
    return render(request, 'index.html', {'results': obj})
def demo(request):
    obj1 = team.objects.all()
    return render(request, 'index.html', {'result': obj1})

