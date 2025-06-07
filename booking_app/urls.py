from django.urls import path
from . import views

urlpatterns = [
    path('', views.resource_list, name='home'),
    path('resources/', views.resource_list, name='resource_list'),
    path('bookings/', views.booking_list, name='booking_list'),
]
