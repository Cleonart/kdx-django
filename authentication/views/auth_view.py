# auth/views.py
from django.contrib.auth import login as django_login
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers import LoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class SessionTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # create Django session and store company info
        user = serializer.user
        django_login(request, user)

        request.session['kdx.company_code'] = request.data.get(
            'company_code', '')
        print('test', request.session['kdx.company_code'])
        print('session:', request.session.items())
        request.session.set_expiry(60 * 60 * 8)  # 8 hours (adjust as needed)
        request.session.cycle_key()              # rotate for security

        return Response(data, status=status.HTTP_200_OK)


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
