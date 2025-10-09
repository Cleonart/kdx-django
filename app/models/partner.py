# -*- coding: utf-8 -*-

from django.db import models
from app.models import Company


class PartnerType(models.TextChoices):
    CUSTOMER = 'customer', 'Customer'
    SUPPLIER = 'supplier', 'Supplier'


class Partner(models.Model):

    class Meta:
        db_table = 'partner'

    company = models.ForeignKey(
        Company,
        on_delete=models.RESTRICT,
        related_name='company_partner_ids')
    code = models.CharField(
        max_length=64,
        unique=True)
    name = models.CharField(max_length=255)
    partner_type = models.CharField(
        choices=PartnerType.choices,
        db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.code} - {self.name}'
