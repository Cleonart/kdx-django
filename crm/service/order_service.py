# -*- coding: utf-8 -*-

from django.db import transaction
from crm.models import Order, OrderLine


class OrderService:

    @transaction.atomic
    def create_one(
            company_id: int,
            customer_id: int,
            order_date,
            notes: str,
            lines: list) -> Order:

        order: Order = Order.objects.create(
            company_id=company_id,
            customer_id=customer_id,
            order_date=order_date,
            notes=notes or "")

        OrderLine.objects.bulk_create([
            OrderLine(order=order, **line) for line in lines
        ])

        return order
