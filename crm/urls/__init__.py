# -*- coding: utf-8 -*-

from django.urls import path
from crm.views import order_view

urlpatterns = [
    path('v1/orders/', order_view.get_order_list, name='order-list'),
]
