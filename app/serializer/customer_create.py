from rest_framework import serializers


class CustomerCreateSerializer(serializers.Serializer):
    company_id = serializers.IntegerField(default=0)
    company_code = serializers.CharField(allow_blank=True)
    code = serializers.CharField(max_length=64)
    name = serializers.CharField(max_length=255)
    partner_type = serializers.ChoiceField(
        choices=[('customer', 'Customer'), ('supplier', 'Supplier')],
        default='customer')
