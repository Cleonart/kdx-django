# -*- coding: utf-8 -*-

from .order_create_line import OrderCreateLineSerializer
from rest_framework import serializers
from crm.models import Order
from crm.models import OrderLine


class OrderCreateSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    customer_id = serializers.IntegerField()
    order_date = serializers.DateField()
    notes = serializers.CharField(allow_blank=True, required=False)
    lines = OrderCreateLineSerializer(many=True)
