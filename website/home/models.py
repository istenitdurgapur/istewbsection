from datetime import datetime
from django.db import models

# Create your models here.


class Gallery(models.Model):
  title = models.CharField(max_length=100)
  image=models.ImageField(upload_to='images/gallery')
  date = models.DateTimeField(default=datetime.today())
  
  def __str__(self):
         return self.title
class carousel(models.Model):
  title = models.CharField(max_length=100)
  image=models.ImageField(upload_to='images/gallery')
  date = models.DateTimeField(default=datetime.today())
  
  def __str__(self):
         return self.title


class Event(models.Model):
  EventName = models.CharField(max_length=100)
  eventDate = models.DateTimeField(default=datetime.today())
  description = models.TextField(max_length=5000,blank=True)
  Image1=models.ImageField(upload_to='images/Events',null = True , blank=True)
  Image2=models.ImageField(upload_to='images/Events',null = True , blank=True)
  Image3=models.ImageField(upload_to='images/Events',null = True , blank=True)
  file1 = models.FileField(upload_to='doc/',null = True , blank=True)
  Link1 = models.CharField(max_length=5000,blank=True)
  file2 = models.FileField(upload_to='doc/',null = True , blank=True)
  Link2 = models.CharField(max_length=5000,blank=True)
  file3 = models.FileField(upload_to='doc/',null = True , blank=True)
  Link3 = models.CharField(max_length=5000,blank=True)
  
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
  image=models.ImageField(upload_to='images/postBearer',null = True , blank=True)
  Post = models.TextField(max_length=100,default=" ")
  details = models.TextField(max_length=100,default=" ")
 
  
  def __str__(self):
         return self.name

class Announcement(models.Model):
  Name = models.CharField(max_length=100)
  Date = models.DateTimeField(default=datetime.today())
  description = models.TextField(max_length=5000,blank=True)
  Link1 = models.CharField(max_length=5000,blank=True,default='#')
  def __str__(self):
         return self.Name