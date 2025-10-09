# -*- coding: utf-8 -*-

from django.db import models


class Partner(models.Model):

    class Meta:
        db_table = 'partner'

    code = models.CharField(
        max_length=64,
        unique=True)
    name = models.CharField(
        max_length=255)
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
