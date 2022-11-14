from django.urls import path
from . import views

app_name="home"

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('events/', views.events, name='events'),
    path('events/detail/<slug:slug>/', views.event_detail, name='event-detail'),
    path('contact-us/', views.contact, name='contact'),
    path('committee/', views.team, name='team'),
    path('executive-council/', views.executiveCouncil, name='executive-council'),

    # About Us
    path('about-iste/', views.about_iste, name='about-iste'),
    path('code-of-conduct/', views.code_of_conduct, name='code-of-conduct'),
    path('objective/', views.objective, name='objective'),
    path('about-section/', views.about_section, name='about-section'),
    path('section-student-chapters/', views.student_chapters, name='student-chapters'),
    path('section-faculty-chapters/', views.faculty_chapters, name='faculty-chapters'),

    # Join ISTE
    path('establish-chapter/', views.establish_chapter, name='establish-chapter'),
    path('establish-student-chapter/', views.establish_student_chapter, name='establish-student-chapter'),
    path('incentive-chapter/', views.incentive_chapter, name='incentive-chapter'),
    path('incentive-student-chapter/', views.incentive_student_chapter, name='incentive-student-chapter'),
]
