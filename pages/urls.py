from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('add_testimonial', views.add_testimonial, name='add_testimonial'),
    path('photos', views.photos, name='photos'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
]
