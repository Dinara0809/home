from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('agent', views.agent, name='agent'),
    path('agentsgrid', views.agentsgrid, name='agentsgrid'),
    path('agentsingle', views.agentsingle, name='agentsingle'),
    path('blogsingle', views.blogsingle, name='blogsingle'),
    path('propertysingle', views.propertysingle, name='propertysingle'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('property', views.property, name='property'),
]
