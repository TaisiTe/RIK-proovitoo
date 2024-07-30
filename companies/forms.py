from django import forms

from .models import Company, Shareholder


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'reg_code', 'date_founded', 'total_capital']
        labels = {
            'name': 'Nimi',
            'reg_code': 'Registrikood',
            'date_founded': 'Asutamiskuupäev',
            'total_capital': 'Kogukapital (€)'
        }

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': '{fieldname} on kohustuslik väli'.format(
                fieldname=field.label)}


class ShareholderForm(forms.ModelForm):
    class Meta:
        model = Shareholder
        fields = ['name', 'code', 'share']
        labels = {
            'name': 'Nimi',
            'share': 'Osakapital (€)',
            'code': 'Isikukood / registrikood'
        }

    def __init__(self, *args, **kwargs):
        super(ShareholderForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': '{fieldname} on kohustuslik väli'.format(
                fieldname=field.label)}


ShareholderFormSet = forms.inlineformset_factory(
    Company, Shareholder,
    form=ShareholderForm,
    extra=1,
    can_delete=True,
)
