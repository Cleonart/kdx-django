from django.db import models
from app.models import Company, Partner


class Order(models.Model):

    class Meta:
        db_table = 'order'

    company = models.ForeignKey(
        Company,
        on_delete=models.RESTRICT,
        related_name='company_order_ids')
    partner = models.ForeignKey(
        Partner,
        on_delete=models.RESTRICT,
        related_name='partner_order_ids')
    order_date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order#{self.id} - {self.customer_name}"
