# -*- coding: utf-8 -*-

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from drf_yasg.utils import swagger_auto_schema
from app.utils.openAPI import openAPIHeadersCompanyCode
from app.serializer import CustomerCreateSerializer, PartnerOutputSerializer
from app.models import Partner


class PaginatedCustomerListSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.CharField(allow_null=True)
    previous = serializers.CharField(allow_null=True)
    results = PartnerOutputSerializer(many=True)


class APICustomer(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['Customers'],
        operation_summary='List Customer',
        operation_description='Returns list of customer',
        responses={
            200: PaginatedCustomerListSerializer,
        })
    def get(self, request):

        records = Partner.objects.all().order_by('id')
        records = records.filter(partner_type='customer')

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(records, request)

        if page is not None:
            ser = PartnerOutputSerializer(page, many=True)
            return paginator.get_paginated_response(ser.data)

        # no pagination (or out of range) -> return full list
        ser = PartnerOutputSerializer(records, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['Customers'],
        request_body=CustomerCreateSerializer,
        responses={201: PartnerOutputSerializer},
        operation_summary='Create customer',
        operation_description='Create new customer record')
    def post(self, request):
        res = CustomerCreateSerializer(data=request.data)
        res.is_valid(raise_exception=True)
        records: Partner = Partner.objects.create(
            code=res.validated_data.get('code'),
            name=res.validated_data.get('name'),
            partner_type=res.validated_data.get('partner_type'))
        return Response(PartnerOutputSerializer(records).data, status=status.HTTP_201_CREATED)
