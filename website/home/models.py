from django.db import models
from django.utils import timezone

class Gallery(models.Model):
  title = models.CharField(max_length=100)
  image=models.ImageField(upload_to='images/gallery')
  date = models.DateField(default=timezone.localdate)

  created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
  
  def __str__(self):
         return self.title

class carousel(models.Model):
  title = models.CharField(max_length=100)
  image=models.ImageField(upload_to='images/gallery')
  date = models.DateField(default=timezone.localdate)

  created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
  
  def __str__(self):
         return self.title
class Event(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateTimeField(default=timezone.now)
  venue = models.CharField(max_length=100, default='Online')
  description = models.TextField(max_length=5000,blank=True)
  
  image1=models.ImageField(upload_to='images/Events',null = True , blank=True)
  image2=models.ImageField(upload_to='images/Events',null = True , blank=True)
  image3=models.ImageField(upload_to='images/Events',null = True , blank=True)

  title_link1 = models.CharField(max_length=200, default='', blank=True)
  url_link1 = models.URLField(blank=True)
  title_link2 = models.CharField(max_length=200, default='', blank=True)
  url_link2 = models.URLField(blank=True)
  title_link3 = models.CharField(max_length=200, default='', blank=True)
  url_link3 = models.URLField(blank=True)
  
  title_file1 = models.CharField(max_length=200, default='', blank=True)
  upload_file1 = models.FileField(upload_to='doc/',null = True , blank=True)
  title_file2 = models.CharField(max_length=200, default='', blank=True)
  upload_file2 = models.FileField(upload_to='doc/',null = True , blank=True)
  title_file3 = models.CharField(max_length=200, default='', blank=True)
  upload_file3 = models.FileField(upload_to='doc/',null = True , blank=True)

  created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
  
  def __str__(self):
         return self.title

class Announcement(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=5000,blank=True)
  link = models.URLField(blank=True)

  created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
  
  def __str__(self):
         return self.title

class Contact(models.Model):
  name = models.CharField(max_length=100)
  phone1 = models.IntegerField(default=9999999999)
  phone2 = models.IntegerField(default=9999999999)
  email = models.EmailField()
  location = models.TextField(max_length=5000,blank=True)

  created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
  
  def __str__(self):
         return self.name

class Post(models.Model):
  title = models.CharField(max_length=100) 
  priority = models.IntegerField(default=0)
  
  def __str__(self):
         return self.title + " (Priority - " + str(self.priority) + ")"
class PostBearer(models.Model):
  name = models.CharField(max_length=100)
  post = models.ForeignKey('Post', null=True, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/PostBearer',null = True, blank=True)
  introduction = models.TextField(max_length=200,default=" ", blank=True, null=True)
  description = models.TextField(max_length=5000,default=" ", blank=True, null=True)  

  created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
  
  def __str__(self):
         return "P " + str(self.post.priority) + " - " + str(self.post.title) + " - " + self.name

class Chapter(models.Model):
  name = models.CharField(max_length=100)
  chapter_code = models.CharField(max_length=100)
  college = models.CharField(max_length=100)
  address = models.TextField(max_length=500)
  email = models.EmailField()

  def __str__(self):
    return str(self.chapter_code) + " - " + str(self.name)

