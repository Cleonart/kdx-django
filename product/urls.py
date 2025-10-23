# -*- coding: utf-8 -*-

from django.urls import path
from product.views import ColorDetailView, ColorListView


urlpatterns = [
    # Colors API Endpoint
    path('v1/colors/', ColorListView.as_view(), name='color-list'),
    path('v1/colors/<int:id>', ColorDetailView.as_view(), name='color-detail'),
]
