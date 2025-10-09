# -*- coding: utf-8 -*-

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from app.serializer import CustomerCreateSerializer, PartnerOutputSerializer
from app.models import Company, Partner


class APICustomer(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=CustomerCreateSerializer,
        responses={201: PartnerOutputSerializer},
        operation_summary='Create customer',
        operation_description='Create new customer record')
    def post(self, request):
        res = CustomerCreateSerializer(data=request.data)
        res.is_valid(raise_exception=True)

        company_id: int = res.validated_data.get('company_id') or None
        company_code: str = res.validated_data.get('company_code') or None
        company = None
        if company_id:
            company = get_object_or_404(Company, id__iexact=company_id)
            company_id = company.id
        elif company_code:
            company_code = company_code.strip()
            company = get_object_or_404(Company, code__iexact=company_code)
            company_id = company.id

        obj = Partner.objects.create(
            company_id=company_id,
            code=res.validated_data.get('code'),
            name=res.validated_data.get('name'),
            partner_type=res.validated_data.get('partner_type'))
        return Response(PartnerOutputSerializer(obj).data, status=status.HTTP_201_CREATED)
