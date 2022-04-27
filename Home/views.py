from django.shortcuts import render, HttpResponse




# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is Homepage")

def about(request):
    return HttpResponse("This is Aboutpage")

def services(request):
    return HttpResponse("This are Servicespage")
# creating these views are when it will go into urls it will come to views and this will appear in page
def contact(request):
    return HttpResponse("This is contactpage")