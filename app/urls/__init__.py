# -*- coding: utf-8 -*-

from django.urls import path
from app.views import company, customer

urlpatterns = [
    path('v1/companies/', company.APICompanies.as_view(), name='api-companies'),
    path('v1/customers/', customer.APICustomer.as_view(), name='api-customer')
]
