# -*- coding: utf-8 -*-

from rest_framework import serializers
from crm.models import Order
from crm.models import OrderLine


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'code', 'name', 'created_at', 'updated_at']
