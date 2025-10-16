# -*- coding: utf-8 -*-
from app.models import Company
from django.contrib.auth.models import User
from django.db import models


class AuthUserCompany(models.Model):

    class Meta:
        db_table = 'auth_user_company'
        unique_together = ('user', 'company_code', 'company')

    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='auth_user_user_ids')
    company = models.ForeignKey(
        Company,
        on_delete=models.RESTRICT,
        related_name='auth_user_company_ids')
    company_code = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s profile"
