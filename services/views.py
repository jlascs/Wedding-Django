from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages, auth


# Create your views here.
def services(request):
    services = Service.objects.order_by('-created_date').filter(is_featured=True)
    paginator = Paginator(services, 4)
    page = request.GET.get('page')
    paged_vanues = paginator.get_page(page)
    city_search = Service.objects.values_list('city', flat=True).distinct()
    state_search = Service.objects.values_list('state', flat=True).distinct()
    service_search = Service.objects.values_list('service_type', flat=True).distinct()
    data = {
        'services' : paged_vanues,
        'city_search' : city_search,
        'state_search' : state_search,
        'service_search' : service_search,
    }
    return render(request, 'pages/services.html', data)


def service_detail(request, id):
    services = Service.objects.all()
    single_service = get_object_or_404(Service, pk=id)
    data = {
        'single_service' : single_service,
        'services' : services,
    }
    return render(request, 'pages/service_detail.html', data)


def add_service(request):
    if request.method == 'POST':
        title = request.POST['title']
        service_type = request.POST['service_type']
        vendor_id = request.POST['vendor_id']
        city = request.POST['city']
        state = request.POST['state']
        featured_package_price = request.POST['featured_package_price']
        service_photo = request.FILES['service_photo']
        service_photo_1 = request.FILES['service_photo_1']
        service_photo_2 = request.FILES['service_photo_2']
        service_photo_3 = request.FILES['service_photo_3']
        service_photo_4 = request.FILES['service_photo_4']
        description = request.POST['description']
        other_details = request.POST['other_details']

        service = Service(title=title, service_type=service_type, vendor_id=vendor_id, city=city, state=state, featured_package_price=featured_package_price,
        service_photo=service_photo, service_photo_1=service_photo_1, service_photo_2=service_photo_2, service_photo_3=service_photo_3, 
        service_photo_4=service_photo_4, description=description, other_details=other_details)
        service.save()
        messages.success(request, 'Added successfully !')
        return redirect('dashboard')
    return render(request, 'accounts/dashboard.html')