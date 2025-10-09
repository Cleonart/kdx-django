# -*- coding: utf-8 -*-

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from crm.serializer import OrderCreateSerializer, OrderOutputSerializer
from crm.service import OrderService


class APIOrders(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=OrderCreateSerializer,
        responses={201: OrderOutputSerializer},
        operation_summary="Create order",
        operation_description="Create new order")
    def post(self, request) -> None:
        data = request.data.copy()
        # cid = request.META.get('HTTP_X_COMPANY_ID')
        # if cid and 'company' not in data:
        #     data['company'] = int(cid)

        order_serialized = OrderCreateSerializer(data=data)
        order_serialized.is_valid(raise_exception=True)

        order = OrderService.create_one(**order_serialized.validated_data)
        return Response(OrderOutputSerializer(order).data, status=status.HTTP_201_CREATED)
