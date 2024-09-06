from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Service (models.Model):

    service_type_choice = (
        ('Photographer', 'Photographer'),
        ('Venue', 'Venue'),
        ('Caterer', 'Caterer'),
        ('Decorator', 'Decorator'),
        ('Makeup', 'Makeup'),
        ('Mehndi', 'Mehndi'),
        ('Pandit', 'Pandit'),
        ('Transport', 'Transport'),
        ('DJ', 'DJ'),
        ('Wedding planner', 'Wedding planner'),
    )

    state_choice = (
        ('Madhaya Pradesh', 'Madhaya Pradesh'),
        ('Kerala', 'Kerala'),
        ('Karnataka', 'Karnataka'),
        ('Maharashtra', 'Maharashtra'),
        ('Punjab', 'Punjab'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
    )

    title = models.CharField(max_length=255)
    service_type = models.CharField(choices=service_type_choice, max_length=100)
    vendor_id =models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(choices=state_choice, max_length=100)
    featured_package_price = models.IntegerField()
    service_photo = models.FileField(upload_to='photos/%y/%m/%d/')
    service_photo_1 = models.FileField(upload_to='photos/%y/%m/%d/', blank=True)
    service_photo_2 = models.FileField(upload_to='photos/%y/%m/%d/', blank=True)
    service_photo_3 = models.FileField(upload_to='photos/%y/%m/%d/', blank=True)
    service_photo_4 = models.FileField(upload_to='photos/%y/%m/%d/', blank=True)
    description = RichTextField()
    other_details = RichTextField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title