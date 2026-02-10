from django.conf import settings
from django.db import models


class Company(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_DEACTIVATED = 'deactivated'
    STATUS_DELETED = 'deleted'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_DEACTIVATED, 'Deactivated'),
        (STATUS_DELETED, 'Deleted'),
    )

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company/logos/',null=True,blank=True)
    address = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='created_companies'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'companies'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
