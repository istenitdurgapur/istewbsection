from django.urls import path
from . import views

app_name="home"

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about, name='about_us'),
    path('gallery/', views.gallery, name='gallery'),
    path('events/', views.events, name='events'),
]
