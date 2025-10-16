from django.db import models
from django.utils import timezone
from app.context import get_current_company


class CompanyQuerySet(models.QuerySet):

    def delete(self):
        """Soft delete - set deleted_at instead of actually deleting"""
        return self.update(deleted_at=timezone.now())

    def hard_delete(self):
        """Actually delete from database"""
        return super().delete()

    def alive(self):
        """Get only non-deleted records"""
        return self.filter(deleted_at__isnull=True)

    def dead(self):
        """Get only deleted records"""
        return self.filter(deleted_at__isnull=False)

    def with_deleted(self):
        """Get all records including deleted"""
        return self

    def for_company(self, company):
        """Filter by specific company"""
        return self.filter(company=company)


class CompanyManager(models.Manager):

    def get_queryset(self):
        """
            Auto-filter by current company
            and exclude soft-deleted
        """
        records = CompanyQuerySet(self.model, using=self._db)

        # Auto-filter by current company
        company = get_current_company()
        if company:
            records = records.filter(company=company)

        # Exclude soft-deleted records
        records = records.filter(deleted_at__isnull=True)
        return records

    def alive(self):
        """
            Alias for get_queryset for clarity
        """
        return self.get_queryset()

    def dead(self):
        """Get soft-deleted records for current company"""
        company = get_current_company()
        records = CompanyQuerySet(self.model, using=self._db).filter(
            deleted_at__isnull=False)
        if company:
            records = records.filter(company=company)
        return records

    def with_deleted(self):
        """
            Get all records (including deleted) for current company
        """
        company = get_current_company()
        records = CompanyQuerySet(self.model, using=self._db)
        if company:
            records = records.filter(company=company)
        return records

    def all_companies(self):
        """
            Get records from ALL companies (admin use)
        """
        return CompanyQuerySet(self.model, using=self._db).filter(deleted_at__isnull=True)


class BaseModel(models.Model):
    """Base model with company filtering and soft delete"""

    company = models.ForeignKey(
        'Company',
        on_delete=models.RESTRICT,
        related_name='%(class)s_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = CompanyManager()
    all_objects = models.Manager()  # Unfiltered access when needed

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """Soft delete - set deleted_at"""
        self.deleted_at = timezone.now()
        self.save(using=using)

    def hard_delete(self, using=None, keep_parents=False):
        """Actually delete from database"""
        super().delete(using=using, keep_parents=keep_parents)

    def restore(self):
        """Restore a soft-deleted record"""
        self.deleted_at = None
        self.save()

    def save(self, *args, **kwargs):
        """Auto-set company on create"""
        if not self.pk and not self.company_id:
            company = get_current_company()
            if company:
                self.company = company
        super().save(*args, **kwargs)
