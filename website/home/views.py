from django.shortcuts import render
from . import models

def home(request):
    return render(request, 'home.html',{})

def about(request):
    return render(request, 'about.html',{})

def gallery(request):
    return render(request, 'gallery.html',{}) 

def events(request):
    events_data = models.Event.objects.all().values()
    return render(request, 'events.html',{'data': events_data}) 

def contact(request):
    return render(request, 'contact-us.html',{})