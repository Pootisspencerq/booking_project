from django.shortcuts import render
from .models import Resource, Booking, Customer

def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'booking_app/resource_list.html', {'resources': resources})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_app/booking_list.html', {'bookings': bookings})
