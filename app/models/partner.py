# -*- coding: utf-8 -*-

from django.db import models
from app.utils.models import BaseModel
from app.models import Company


class PartnerType(models.TextChoices):
    CUSTOMER = 'customer', 'Customer'
    SUPPLIER = 'supplier', 'Supplier'


class Partner(BaseModel):

    class Meta:
        db_table = 'partner'

    code = models.CharField(
        max_length=64,
        unique=True)
    name = models.CharField(max_length=255)
    partner_type = models.CharField(
        choices=PartnerType.choices,
        db_index=True)

    def __str__(self):
        return f'{self.code} - {self.name}'
