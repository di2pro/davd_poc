from django.db import models
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
    is_enabled = models.BooleanField(default=True, null=False)
    name = models.CharField(null=False, blank=False, max_length=120)
    created_at = models.DateTimeField(auto_created=True)
    disabled_at = models.DateTimeField(null=True, blank=True)


class User(AbstractUser):
    is_enabled = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_created=True)
    disabled_at = models.DateTimeField(null=True, blank=True)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='members')
