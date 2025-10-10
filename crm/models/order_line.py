# -*- coding: utf-8 -*-

from django.db import models
from .order import Order
from django.core.validators import MinValueValidator
from decimal import Decimal

class OrderLine(models.Model):

    class Meta:
        db_table = 'crm_order_line'

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='lines')
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))]
    )

    @property
    def line_total(self):
        return self.quantity * self.unit_price
