from django.db import models


class Company(models.Model):

    class Meta:
        db_table = 'company'

    code = models.CharField(
        max_length=64,
        unique=True)
    name = models.CharField(
        max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
