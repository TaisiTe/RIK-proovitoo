import pytest

from companies.models import Company

pytestmark = pytest.mark.django_db


class TestCompanyModel:

    def test_save_company(self):
        company = Company.objects.create(
            name='Viktori Saladus OÜ',
            reg_code='1234567',
            total_capital=2500
        )
        assert company.name == 'Viktori Saladus OÜ'
        assert company.total_capital == 2500
