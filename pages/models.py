from email import message
from statistics import mode
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from datetime import datetime

# Create your models here.

class AboutImage (models.Model):
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/')

class Team (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    facebook_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    linkedin_link = models.URLField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

############################################################################################

class Contact (models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


################################################################################################

class Review (models.Model):
    bride_name = models.CharField(max_length=50)
    groom_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    description = models.TextField(max_length=1000)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.bride_name

###############################################################################################


class Image (models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

#################################################################################################
