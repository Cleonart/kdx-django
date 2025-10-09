# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from crm.serializer import OrderCreateSerializer
from crm.service import OrderService


class APIOrders(APIView):
    permission_classes = [AllowAny]

    def post(self, request) -> None:
        # If you scope company from header, inject it before validation
        data = request.data.copy()
        cid = request.META.get('HTTP_X_COMPANY_ID')
        if cid and 'company' not in data:
            data['company'] = int(cid)

        order_serialized = OrderCreateSerializer(data=data)
        order_serialized.is_valid(raise_exception=True)

        order = OrderService.create_one(**order_serialized.validated_data)
        return Response(OrderOut(order).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_order_list(request):
    return Response({
        'test': 'test CRM'
    }, status=status.HTTP_200_OK)
