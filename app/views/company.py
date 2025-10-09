# -*- coding: utf-8 -*-

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from app.serializer import CompanyListSerializer
from app.models import Company
from common.openAPI import openAPIParamsInQueryAsStr, openAPIParamsInQueryAsInt

# --- For nice paginated schema in Swagger ---


class PaginatedCompanyListSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.CharField(allow_null=True)
    previous = serializers.CharField(allow_null=True)
    results = CompanyListSerializer(many=True)


class APICompanies(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openAPIParamsInQueryAsStr('code', 'Filter by company code'),
            openAPIParamsInQueryAsStr('name', 'Filter by company name'),
            openAPIParamsInQueryAsInt('page', 'Current Page'),
            openAPIParamsInQueryAsInt('page_size', 'Page Size')],
        operation_summary='List companies',
        operation_description='Returns a paginated list of companies filtered by optional `name` and `code`.',
        responses={
            200: PaginatedCompanyListSerializer,   # when paginated
        })
    def get(self, request):

        # safely read query params
        filter_name = request.query_params.get('name')
        filter_code = request.query_params.get('code')

        # start from base queryset (not list)
        records = Company.objects.all().order_by('id')

        # chain filters on the same queryset
        if filter_code:
            records = records.filter(code__icontains=filter_code.strip())
        if filter_name:
            records = records.filter(name__icontains=filter_name.strip())

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(records, request)

        if page is not None:
            ser = CompanyListSerializer(page, many=True)
            return paginator.get_paginated_response(ser.data)

        # no pagination (or out of range) -> return full list
        ser = CompanyListSerializer(records, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        # change to your "create" serializer if different
        request_body=CompanyListSerializer,
        responses={201: CompanyListSerializer},
        operation_summary="Create company",
        operation_description="Create a company record.")
    def post(self, request):
        # Example create flow (adjust to your real serializer/fields)
        serializer = CompanyListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(CompanyListSerializer(obj).data, status=status.HTTP_201_CREATED)
