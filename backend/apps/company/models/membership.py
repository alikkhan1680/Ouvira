from django.conf import settings
from django.db import models

from .company import Company
from .role import Role


class UserCompany(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='company_memberships'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='members'
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT
    )

    is_primary_company = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_companies'
        unique_together = ('user', 'company')

    def __str__(self):
        return f'{self.user} - {self.company} ({self.role})'
