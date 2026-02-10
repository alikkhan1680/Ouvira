from django.db import models

from .company import Company


class CompanySettings(models.Model):
    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        related_name='settings'
    )

    default_language = models.CharField(max_length=10, default='en')
    default_currency = models.CharField(max_length=10, default='USD')
    timezone = models.CharField(max_length=50, default='UTC')
    fiscal_year_start_month = models.PositiveSmallIntegerField(default=1)

    feature_flags = models.JSONField(default=dict, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'company_settings'

    def __str__(self):
        return f'Settings for {self.company}'
