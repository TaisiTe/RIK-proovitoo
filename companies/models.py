from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def only_int(value):
    if not value.isdigit():
        raise ValidationError('Registrikood peab koosnema ainult numbritest.')


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True,
                            validators=[MinLengthValidator(3, 'Osaühingu nimi peab koosnema vähemalt '
                                                              'kolmest tähest või numbrist.')],
                            error_messages={'unique': 'Sellise nimega osaühing on juba olemas.'})
    reg_code = models.CharField(validators=[only_int, MinLengthValidator(6,
                                                                         'Registrikood peab koosnema '
                                                                         'seitsmest numbrist.'),
                                            MaxLengthValidator(100, 'Osaühingu nimi ei tohi olla '
                                                                    'pikem kui 100 tähte või numbrit.')],
                                unique=True, max_length=7,
                                error_messages={'unique': 'Sellise registrikoodiga osaühing on juba olemas.'})
    date_founded = models.DateField(default=date.today(),
                                    validators=[MaxValueValidator(date.today(), 'Kuupäev peab olema väiksem või '
                                                                                'võrdne käesoleva kuupäevaga.')])
    total_capital = models.IntegerField(null=False,
                                        validators=[MinValueValidator(2500, 'Kogukapitali suurus '
                                                                            'peab olema vähemalt 2500€.')])
    date_created = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name


class Shareholder(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, default='')
    share = models.IntegerField(null=False,
                                validators=[MinValueValidator(1,
                                                              'Osakapitali suurus peab olema vähemalt 1€.')])
    is_founder = models.BooleanField(default=False)
    date_created = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return self.name
