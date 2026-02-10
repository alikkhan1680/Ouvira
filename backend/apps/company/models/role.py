from django.db import models


class Role(models.Model):
    OWNER = 'owner'
    ADMIN = 'admin'
    HR = 'hr'
    USER = 'user'

    ROLE_CHOICES = (
        (OWNER, 'Owner'),
        (ADMIN, 'Admin'),
        (HR, 'HR Manager'),
        (USER, 'User'),
    )

    name = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        unique=True
    )

    is_system_role = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.name
