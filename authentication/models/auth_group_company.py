# -*- coding: utf-8 -*-
from app.models import Company
from django.contrib.auth.models import Group
from django.db import models


class AuthGroupCompany(models.Model):

    class Meta:
        db_table = 'auth_group_company'
        unique_together = ('group', 'company')

    group = models.ForeignKey(
        Group,
        on_delete=models.RESTRICT,
        related_name='auth_user_group_ids')
    company = models.ForeignKey(
        Company,
        on_delete=models.RESTRICT,
        related_name='auth_user_group_company_ids')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.group.name}'s"
