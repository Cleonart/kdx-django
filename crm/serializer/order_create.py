# -*- coding: utf-8 -*-

from .order_create_line import OrderCreateLineSerializer
from rest_framework import serializers
from crm.models import Order
from crm.models import OrderLine


class OrderCreateSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    company_code = serializers.CharField(allow_blank=True)
    customer_id = serializers.IntegerField()
    customer_code = serializers.CharField(allow_blank=True)
    order_date = serializers.DateTimeField()
    notes = serializers.CharField(allow_blank=True, required=False)
    lines = OrderCreateLineSerializer(many=True)
