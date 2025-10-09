# -*- coding: utf-8 -*-

from django.urls import path
from app.views import company

urlpatterns = [
    path('v1/companies/', company.APICompanies.as_view(), name='api-companies'),
]
