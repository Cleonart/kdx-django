from app.utils.models import BaseModel
from django.db import models


class ProductAttrSize(BaseModel):

    class Meta:
        db_table = 'product_attr_size'
        indexes = [models.Index(fields=['company', 'code'])]
        constraints = [
            models.UniqueConstraint(
                fields=['company', 'code'],
                name='uniq_size_code')]

    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
