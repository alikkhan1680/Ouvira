import uuid

from django.conf import settings
from django.db import models

from .company import Company
from .role import Role


class Invitation(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_ACCEPTED = 'accepted'
    STATUS_EXPIRED = 'expired'
    STATUS_CANCELED = 'canceled'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_ACCEPTED, 'Accepted'),
        (STATUS_EXPIRED, 'Expired'),
        (STATUS_CANCELED, 'Canceled'),
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='invitations'
    )
    email = models.EmailField()
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT
    )

    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )

    expires_at = models.DateTimeField()

    invited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='sent_invitations'
    )
    accepted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='accepted_invitations'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'invitations'
        unique_together = ('company', 'email')

    def __str__(self):
        return f'Invite {self.email} to {self.company}'
