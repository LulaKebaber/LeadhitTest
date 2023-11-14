from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from .models import FormTemplate


class FormAPITestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def setUp(self):
        # Form 1
        self.registration_form = FormTemplate.objects.create(
            name='registration_form',
            fields={
                "username": "text",
                "email": "email",
                "password": "text",
                "user_phone": "phone",
                "created_date": "date"
            })

        # Form 2
        self.contact_form = FormTemplate.objects.create(
            name='contact_form',
            fields={
                "name": "text",
                "contact_email": "email",
                "contact_phone": "phone",
            })

        # Form 3
        self.appointment_form = FormTemplate.objects.create(
            name='appointment_form',
            fields={
                "patient_name": "text",
                "patient_phone": "phone",
                "appointment_date": "date",
            })

        # Form 4
        self.feedback_form = FormTemplate.objects.create(
            name='feedback_form',
            fields={
                "username": "email",
                "user_phone": "phone",
                "feedback_date": "date",
                "message": "text",
            })

        # Form 5
        self.order_form = FormTemplate.objects.create(
            name='order_form',
            fields={
                "username": "text",
                "user_phone": "phone",
                "order_date": "date",
                "user_email": "email",
            })

    def test_registration_form(self):
        url = "http://localhost:8000/api/get_form?username=abc&email=b@mail.ru&password=pass&user_phone=%2B7%20700%20700%2070%2070&created_date=2022-10-10"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], 'registration_form')