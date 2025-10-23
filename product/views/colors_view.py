# -*- coding: utf-8 -*-

from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from app.utils.openAPI import openAPIParamsInQueryAsStr, openAPIParamsInQueryAsInt
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from product.models import ProductAttrColor
from product.serializers import ProductAttrColorCreateSerializer


class ColorListView(APIView):
    """
        URL: /api/v1/products/colors/
        Methods: GET, POST
        Description: API endpoints for managing product colors
    """

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['Product Colors'],
        manual_parameters=[
            openAPIParamsInQueryAsStr('code', 'Filter by color code'),
            openAPIParamsInQueryAsStr('name', 'Filter by color name'),
            openAPIParamsInQueryAsInt('page', 'Current Page'),
            openAPIParamsInQueryAsInt('page_size', 'Page Size')],
        responses={200: ProductAttrColorCreateSerializer},
        operation_summary='List product colors',
        operation_description='Retrieve a list of product colors')
    def get(self, request) -> Response:
        colors = ProductAttrColor.objects.all()
        return Response(data=colors, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['Product Colors'],
        request_body=ProductAttrColorCreateSerializer,
        operation_summary='Create product color',
        operation_description='Create a new product color',
        responses={201: ProductAttrColorCreateSerializer})
    def post(self, request) -> Response:
        res = ProductAttrColorCreateSerializer(data=request.data)
        res.is_valid(raise_exception=True)
        records: ProductAttrColor = ProductAttrColor.objects.create(
            code=res.validated_data.get('code'),
            name=res.validated_data.get('name'))
        return Response(data=ProductAttrColorCreateSerializer(records).data, status=status.HTTP_201_CREATED)


class ColorDetailView(APIView):
    """
        URL: /api/v1/products/colors/:color_id
        Methods: GET, PATCH
        Description: API endpoints for retrieving and updating a specific product color
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['Product Colors'],
        responses={200: ProductAttrColorCreateSerializer},
        operation_summary='Retrieve product color',
        operation_description='Retrieve a specific product color by ID')
    def get(self, request, color_id: int) -> Response:
        color = get_object_or_404(ProductAttrColor, id=color_id)
        return Response(data=color, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['Product Colors'],
        responses={200: ProductAttrColorCreateSerializer},
        request_body=ProductAttrColorCreateSerializer,
        operation_summary='Update product color',
        operation_description='Update a specific product color by ID')
    def patch(self, request, color_id: int) -> Response:
        data = request.data.copy()
        color = get_object_or_404(ProductAttrColor, id=color_id)
        res = ProductAttrColor(color, data=data, partial=True)
        res.is_valid(raise_exception=True)
        res.save()
        return Response(data=res, status=status.HTTP_200_OK)
