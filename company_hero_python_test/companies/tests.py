from rest_framework.test import APITestCase
from rest_framework import status
class CompanyTestCase(APITestCase):

    def test_create_company_whitout_name(self):
        data = {
            "cnpj": "123.456.789",
        }
        response = self.client.post('/api/company/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_company_correctly(self):
        data = {
            "cnpj": "123.456.789",
            "name": "Company Hero"
        }
        response = self.client.post('/api/company/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_company_employees(self):
        response = self.client.get('/api/company/users?company=Company Hero')
        self.assertEqual(response.status_code, status.HTTP_200_OK)