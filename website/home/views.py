from django.shortcuts import render
from . import models
from datetime import datetime
from django.urls import reverse_lazy

def home(request):
    today = datetime.now()
    chairman = models.PostBearer.objects.all().filter(post__priority=1).first()
    secretary = models.PostBearer.objects.all().filter(post__priority=2).first()
    carousel_data = models.carousel.objects.all().order_by('-date')
    announcements = models.Announcement.objects.all().order_by('-date')[:5]
    upcoming_events = models.Event.objects.all().filter(date__gte=today)[:5]
    past_events = models.Event.objects.all().filter(date__lt=today)[:(5-len(upcoming_events))]
    context = {
        'announcements': announcements, 
        'chairman':chairman, 
        'secretary':secretary, 
        'c_data': carousel_data, 
        'upcoming_events':upcoming_events,
        'past_events':past_events
    }
    return render(request, 'home.html',context)

def about_iste(request):
    return render(request, 'iste/about_iste.html',{})

def about_section(request):
    return render(request, 'section/about_section.html',{})

def code_of_conduct(request):
    return render(request, 'iste/code_of_conduct.html',{})

def objective(request):
    return render(request, 'iste/objective.html',{})

def chapters(request):
    chapters = models.Chapter.objects.all()
    return render(request, 'section/chapters.html',{'chapters':chapters})

def gallery(request):
    images = models.Gallery.objects.all().order_by('-date')
    return render(request, 'gallery.html',{'images': images}) 

def events(request):
    today = datetime.now()
    upcoming_events = models.Event.objects.all().filter(date__gte=today).order_by('-date')
    past_events = models.Event.objects.all().filter(date__lt=today).order_by('-date')
    return render(request, 'events.html',{'upcoming_events': upcoming_events, 'past_events':past_events})

def event_detail(request, slug):
    q = models.Event.objects.filter(slug__iexact = slug)
    if q.exists():
        q = q.first()
    else:
        return reverse_lazy('events')
    return render(request, 'event_details.html', {'event': q})

def team(request):
    members = models.PostBearer.objects.all().order_by('post__priority')
    return render(request, 'team.html',{'members':members})

def executiveCouncil(request):
    members = models.PostBearer.objects.all().order_by('post__priority')
    return render(request, 'executive_council.html',{'members':members})

def contact(request):
    contact = models.Contact.objects.all().first()
    return render(request, 'contact-us.html',{'contact':contact})

def establish_chapter(request):
    return render(request, 'join_iste/establish_chapter.html',{})

def incentive_chapter(request):
    return render(request, 'join_iste/incentive_chapter.html',{})

def establish_student_chapter(request):
    return render(request, 'join_iste/establish_student_chapter.html',{})

def incentive_student_chapter(request):
    return render(request, 'join_iste/incentive_student_chapter.html',{})