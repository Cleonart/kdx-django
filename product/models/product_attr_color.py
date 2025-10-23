from app.utils.models import BaseModel
from django.db import models


class ProductAttrColor(BaseModel):

    class Meta:
        db_table = 'product_attr_color'
        indexes = [models.Index(fields=['company', 'code'])]
        constraints = [
            models.UniqueConstraint(
                fields=['company', 'code'],
                name='uniq_color_code')]

    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
