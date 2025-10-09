from rest_framework import serializers
from app.models import Partner


class PartnerOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ['id', 'code', 'name', 'created_at', 'updated_at']
