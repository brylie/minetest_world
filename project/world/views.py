from django.shortcuts import render
from django.views import generic

from .models import World

# Create your views here.
class IndexView(generic.ListView):
    model = World
    template_name = 'world/index.html'
