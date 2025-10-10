# -*- coding: utf-8 -*-

from rest_framework import serializers
from crm.models import Order
from crm.models import OrderLine


class OrderOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'company_id', 'customer_id',
                  'order_date', 'notes', "lines"]
