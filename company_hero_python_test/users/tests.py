from rest_framework.test import APITestCase
from rest_framework import status
class UserTestCase(APITestCase):

    def test_create_user_whitout_password_or_email(self):
        data = {
            "first_name": "gabriel",
            "last_name": "boian"
        }
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_correctly(self):
        data = {
            "email": "teste@companyhero.com",
            "password": "123",
            "first_name": "company",
            "last_name": "hero"
        }
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employee_companies_list(self):
        response = self.client.get('/api/users/list-companies/gabriel@teste.com.br')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_of_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)