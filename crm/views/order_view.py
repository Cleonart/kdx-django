# -*- coding: utf-8 -*-

from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from app.utils.openAPI import openAPIHeadersCompanyCode
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from crm.serializer import OrderCreateSerializer, OrderOutputSerializer
from crm.service import OrderService
from app.models import Company
from app.models import Partner


class APIOrders(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=OrderCreateSerializer,
        manual_parameters=[openAPIHeadersCompanyCode()],
        responses={201: OrderOutputSerializer},
        operation_summary="Create order",
        operation_description="Create new order")
    def post(self, request) -> None:
        data = request.data.copy()
        # cid = request.META.get('HTTP_X_COMPANY_ID')
        # if cid and 'company' not in data:
        #     data['company'] = int(cid)

        res = OrderCreateSerializer(data=data)
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

        customer_id: int = res.validated_data.get('customer_id') or None
        customer_code: str = res.validated_data.get('customer_code') or None
        customer = None
        if customer_id:
            customer = get_object_or_404(Partner, id__iexact=customer_id)
            customer_id = customer.id
        elif customer_code:
            customer_code = customer_code.strip()
            customer = get_object_or_404(Partner, code__iexact=customer_code)
            customer_id = customer.id

        res.validated_data.pop('company_code', '')
        res.validated_data.pop('customer_code', '')
        res.validated_data.company_id = company_id
        data_dict: dict = {**res.validated_data}
        data_dict['company_id'] = company_id
        data_dict['customer_id'] = customer_id

        order = OrderService.create_one(**data_dict)
        return Response(OrderOutputSerializer(order).data, status=status.HTTP_201_CREATED)
