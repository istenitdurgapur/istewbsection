from datetime import datetime
from django.db import models

# Create your models here.


class Gallery(models.Model):
  title = models.CharField(max_length=100)
  image=models.ImageField(upload_to='images/gallery')
  date = models.DateTimeField(default=datetime.today())
  
  def __str__(self):
         return self.title


class Event(models.Model):
  EventName = models.CharField(max_length=100)
  eventDate = models.DateTimeField(default=datetime.today())
  description = models.TextField(max_length=5000,blank=True)
  Image1=models.ImageField(upload_to='images/Events')
  Image2=models.ImageField(upload_to='images/Events')
  Image3=models.ImageField(upload_to='images/Events')
  file1 = models.FileField(upload_to='doc/')
  Link1 = models.CharField(max_length=5000,blank=True,default=" ")
  file2 = models.FileField(upload_to='doc/')
  Link2 = models.CharField(max_length=5000,blank=True,default=" ")
  file3 = models.FileField(upload_to='doc/')
  Link3 = models.CharField(max_length=5000,blank=True,default=" ")
  
  def __str__(self):
         return self.EventName

class Contact(models.Model):
  name = models.CharField(max_length=100)
  phone1 = models.IntegerField(default=1234567890)
  phone2 = models.IntegerField(default=1234567890)
  email = models.EmailField()
  location = models.TextField(max_length=5000,blank=True)
  
  def __str__(self):
         return self.name


class PostBearer(models.Model):
  name = models.CharField(max_length=100)
  Post = models.TextField(max_length=100,default=" ")
  details = models.TextField(max_length=100,default=" ")
 
  
  def __str__(self):
         return self.name

