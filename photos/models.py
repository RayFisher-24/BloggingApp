from django.db import models
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
# Create your models here.

class photo(models.Model):
   
   name = models.CharField(max_length=100)
   img = models.ImageField(upload_to='pics')
   alt = models.CharField(max_length=20, default="None")
   offer = models.BooleanField(default=False)
   
   def get_absolute_url(self):
      return reverse("post:details", kwargs={"pk": self.pk}) 

   class Meta:
    ordering = ["-pk"]

class wedding(models.Model):
   
   name = models.CharField(max_length=100)
   img = models.ImageField(upload_to='pics')
   alt = models.CharField(max_length=20, default="None")

   def get_absolute_url(self):
      return reverse("post:details", kwargs={"pk": self.pk}) 

   class Meta:
    ordering = ["-pk"]

class Contact(models.Model):
   
   name = models.CharField(max_length=30)
   email = models.CharField(max_length=50, default="None")
   phone = models.CharField(max_length=12, default="None")
   message = models.CharField(max_length=120, default="None")

class Article(models.Model):

   title = models.CharField(max_length=200)
   date = models.DateField()
   head1 = models.TextField(max_length=200, default='')
   head2 = models.TextField(max_length=500, default='')
   head3 = models.TextField(max_length=1000, primary_key=True)
   image1 = models.ImageField(upload_to='pics', default='')
   image2 = models.ImageField(upload_to='pics', default='')
   image3 = models.ImageField(upload_to='pics', default='')
   alt = models.CharField(max_length=20, default="None")
   writter = models.CharField(max_length=50)
   slug = models.SlugField(max_length=150, unique=True)
   avater = models.ImageField(upload_to='pics', default='')
   bio = models.TextField(max_length=250, default='')
   
     
   def get_absolute_url(self):
      return reverse("single_page", kwargs={"slug": self.slug}) 

   class Meta:
    unique_together = ('slug', 'title') 
    ordering = ["-pk"]
