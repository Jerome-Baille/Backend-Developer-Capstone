from django.shortcuts import render
from .forms import BookingForm
from .models import Menu, Booking
from django.core import serializers
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import BookingSerializer, MenuSerializer


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class menu(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class menu_item(RetrieveUpdateAPIView, DestroyAPIView): 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class bookings(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})
