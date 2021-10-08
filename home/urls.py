from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('agent', views.agent, name='agent'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('properties', views.property, name='properties'),
]
