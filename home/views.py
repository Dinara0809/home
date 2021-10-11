from django.shortcuts import render, redirect
from .models import *


def about(request):
    return render(request, 'about.html')


def agentsingle(request):
    return render(request, 'agent-single.html')

def agentsgrid(request):
    return render(request, 'agents-grid.html')


def agent(request):
    return render(request, 'agent.html')


def blog(request):
    return render(request, 'blog-grid.html')


def blogsingle(request):
    return render(request, 'blog-single.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')



def propertysingle(request):
    return render(request, 'property-single.html')


def property(request):
    return render(request, 'property.html')


def home(request):
    home = Home.objects.all()
    return render(request, 'property.html', 'propertysingle', {'home': home})


