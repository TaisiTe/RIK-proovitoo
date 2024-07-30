from django.test import TestCase
from .models import Company, Shareholder


class CompanyTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Test Company', reg_code='7654321', total_capital=2500)

    def test_company_creation(self):
        self.assertEqual(self.company.name, 'Test Company')
        self.assertEqual(self.company.reg_code, '7654321')
        self.assertEqual(self.company.total_capital, 2500)
