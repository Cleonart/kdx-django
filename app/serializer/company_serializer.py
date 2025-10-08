from rest_framework import serializers
from app.models import Company


class CompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'code', 'name', 'created_at', 'updated_at']
