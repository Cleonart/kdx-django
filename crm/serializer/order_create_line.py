from rest_framework import serializers
from decimal import Decimal

class OrderCreateLineSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField(min_value=1)
    unit_price = serializers.DecimalField(
        max_digits=12, decimal_places=2, min_value=Decimal("0.00"), coerce_to_string=False,  # <- key! keep it as a JSON number
    )
