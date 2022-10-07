from django.urls import path
from . import views

app_name="home"

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about-us'),
    path('gallery/', views.gallery, name='gallery'),
    path('events/', views.events, name='events'),
    path('contact-us/', views.contact, name='contact'),
]
