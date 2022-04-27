from django.contrib import admin
from django.urls import path 
from Home import views
urlpatterns = [
    #this are he tabs which will be open after we type 8000/.......
    path("home",views.index, name='index'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    
]
