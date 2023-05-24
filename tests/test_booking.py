from django.urls import reverse
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from datetime import date
import json

from restaurant.models import Booking
from restaurant.serializers import BookingSerializer

class BookingViewSetTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

        self.booking1 = Booking.objects.create(
            first_name='John Doe',
            reservation_date=date(2023, 5, 27),
            reservation_slot=6
        )
        self.booking2 = Booking.objects.create(
            first_name='Jane Smith',
            reservation_date=date(2023, 5, 28),
            reservation_slot=8
        )
        self.valid_payload = {
            'first_name': 'Test Booking',
            'reservation_date': str(date.today()),
            'reservation_slot': 3
        }
        self.invalid_payload = {
            'first_name': '',
            'reservation_date': '',
            'reservation_slot': ''
        }

    def test_get_all_bookings(self):
        response = self.client.get(reverse('booking-list'))
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_booking(self):
        response = self.client.post(
            reverse('booking-list'),
            data=json.dumps(self.valid_payload, cls=DjangoJSONEncoder),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_booking(self):
        response = self.client.post(
            reverse('booking-list'),
            data=json.dumps(self.invalid_payload, cls=DjangoJSONEncoder),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_valid_single_booking(self):
        response = self.client.get(reverse('booking-detail', kwargs={'pk': self.booking1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        booking = Booking.objects.get(pk=self.booking1.pk)
        serializer = BookingSerializer(booking)
        self.assertEqual(response.data, serializer.data)
