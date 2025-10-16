# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from ..serializers import UserSerializer, UserCreateSerializer


class UserViewAPI(APIView):
    """
        Get current authenticated user information
        Requires: JWT Token
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({
            'success': True,
            'data': serializer.data
        })
