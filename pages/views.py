from ast import keyword
import imp
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from .models import AboutImage, Contact, Team, Review, Image
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from services.models import Service
from accounts.models import Vendor
# Create your views here.

def handler404(request, exception=None):
    return render(request, 'includes/404.html')

def home(request):
    teams = Team.objects.all()
    featured_services = Service.objects.order_by('-created_date').filter(is_featured=True)
    all_services = Service.objects.order_by('-created_date').filter(is_featured=True)
    city_search = Service.objects.values_list('city', flat=True).distinct()
    state_search = Service.objects.values_list('state', flat=True).distinct()
    service_search = Vendor.objects.values_list('service_type', flat=True).distinct()
    data = {
        'teams' : teams,
        'featured_services' : featured_services,
        'city_search' : city_search,
        'state_search' : state_search,
        'service_search' : service_search,
        'all_services' : all_services,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    images = AboutImage.objects.all()
    data = {
        'teams' : teams,
        'images' : images,
    }
    return render(request, 'pages/about.html', data)

def testimonials(request):
    vendors = Vendor.objects.filter(user=request.user.id)
    reviews = Review.objects.all().filter(is_featured=True)
    if vendors:
        is_vendor = True
        vendor = vendors[0]
    else:
        is_vendor = False
        vendor = None
    data = {
        'is_vendor': is_vendor,
        'vendor' : vendor,
        'reviews' : reviews,
    }
    return render(request, 'pages/testimonials.html', data)

def add_testimonial(request):
    if request.method == 'POST':
        bride_name = request.POST['bride_name']
        groom_name = request.POST['groom_name']
        city = request.POST['city']
        photo = request.FILES['photo']
        description = request.POST['description']

        add_review = Review(bride_name=bride_name, groom_name=groom_name, city=city, photo=photo, description=description)
        add_review.save()
        messages.success(request, 'Added successfully !')
        return redirect('testimonials')
    return render(request, 'pages/testimonials.html')

def photos(request):
    images = Image.objects.all().filter(is_featured=True)
    data = {
        'images' : images,
    }
    return render(request, 'pages/photos.html', data)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, phone=phone, message=message)
        contact.save()
        messages.success(request, 'Thankyou for contacting us. we will get back to you soon !')
        return redirect('contact')
    return render(request, 'pages/contact.html')


def search(request):
    services = Service.objects.order_by('-created_date').filter(is_featured=True)
    city_search = Service.objects.values_list('city', flat=True).distinct()
    state_search = Service.objects.values_list('state', flat=True).distinct()
    service_search = Service.objects.values_list('service_type', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            services = services.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            services = services.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            services = services.filter(state__iexact=state)
    
    if 'service_type' in request.GET:
        service_type = request.GET['service_type']
        if service_type:
            services = services.filter(service_type__iexact=service_type)

    if 'min_featured_package_price' in request.GET:
        min_featured_package_price = request.GET['min_featured_package_price']
        max_featured_package_price = request.GET['max_featured_package_price']
        if max_featured_package_price:
           services = services.filter(featured_package_price__gte=min_featured_package_price, featured_package_price__lte=max_featured_package_price)
    data = {
        'services' : services,
        'city_search' : city_search,
        'state_search' : state_search,
        'service_search' : service_search,
    }
    return render(request, 'pages/search.html', data)