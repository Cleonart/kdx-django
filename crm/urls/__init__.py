# -*- coding: utf-8 -*-

from django.urls import path
from crm.views import order_view

urlpatterns = [
    path('v1/orders/', order_view.APIOrders.as_view(), name='order-list'),
]
