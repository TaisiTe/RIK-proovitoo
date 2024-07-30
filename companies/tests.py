from django.test import TestCase
from .models import Company, Shareholder


class CompanyModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Test Company', reg_code='7654321', total_capital=2500)

    def test_company_creation(self):
        self.assertEqual(self.company.name, 'Test Company')
        self.assertEqual(self.company.reg_code, '7654321')
        self.assertEqual(self.company.total_capital, 2500)


class ShareholderModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Test Company', reg_code='7654321', total_capital=2500, id=1)
        self.shareholder = Shareholder.objects.create(name='Test Shareholder', code='7654321', share=2500,
                                                      company=self.company)

    def test_shareholder_creation(self):
        self.assertEqual(self.shareholder.name, 'Test Shareholder')
        self.assertEqual(self.shareholder.code, '7654321')
        self.assertEqual(self.shareholder.share, 2500)
        self.assertEqual(self.shareholder.company_id, 1)

# TODO: Add more tests to cover all code
