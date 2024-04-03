from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('events/', EventsAPI.as_view()),
    path('bookings/', BookingsAPI.as_view()),
    # path('register/', UserRegistrationView.as_view()),
    path('organiser/', EventOrganiserAPI.as_view()),
    path('customer/', CustomerAPI.as_view()),
    path('ticket/', TicketAPI.as_view()),
    
]
