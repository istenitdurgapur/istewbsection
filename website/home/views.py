from django.shortcuts import render
from . import models

def home(request):
    events_data = models.Event.objects.all().values()
    return render(request, 'home.html',{'data': events_data})

def about(request):
    return render(request, 'about.html',{})

def gallery(request):
    data = models.Gallery.objects.all().values()
    return render(request, 'gallery.html',{'data': data}) 

def events(request):
    events_data = models.Event.objects.all().values()
    return render(request, 'events.html',{'data': events_data}) 

def contact(request):
    contact_data = models.Contact.objects.all().values()
    return render(request, 'contact-us.html',{'data':contact_data})