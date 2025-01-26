# api/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Patient


class TestLogin(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='doctor1', password='password123', role='doctor')

    def test_login(self):
        response = self.client.post('/api/login/', {'username': 'doctor1', 'password': 'password123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)


class TestPatientList(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.doctor = get_user_model().objects.create_user(username='doctor1', password='password123', role='doctor')
        self.patient = Patient.objects.create(first_name="John", last_name="Doe", date_of_birth="1990-01-01", doctor=self.doctor)

    def test_patient_list(self):
        # Авторизуемся
        response = self.client.post('/api/login/', {'username': 'doctor1', 'password': 'password123'})
        access_token = response.data['access_token']

        # Делаем запрос с токеном
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
