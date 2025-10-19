from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginSerializer(TokenObtainPairSerializer):
    company_code = serializers.CharField(required=False, allow_blank=True)

    @classmethod
    def get_token(cls, user):
        # Do NOT add company here (you want it in session only)
        return super().get_token(user)
