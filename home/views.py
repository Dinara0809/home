from django.shortcuts import render, redirect
from .models import *


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def agent(request):
    return render(request, 'agent.html')


def blog(request):
    return render(request, 'blog-grid.html')


def contact(request):
    return render(request, 'contact.html')


def property(request):
    return render(request, 'property.html')


# def propertys(request):
#     return render(request, 'propertys.html')

def agentsgrid(request):
    return render(request, 'agents-grid.html')


def agent(request):
    agent = Agent.objects.all()
    return render(request, 'index.html', {'agent': agent})


def home(request):
    home = Home.objects.all()
    return render(request, 'property.html', {'home': home})
