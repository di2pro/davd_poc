from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Organization(models.Model):
    is_enabled = models.BooleanField(default=True, null=False)
    name = models.CharField(null=False, blank=False, max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    disabled_at = models.DateTimeField(null=True, blank=True)


class User(AbstractUser):
    is_enabled = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    disabled_at = models.DateTimeField(null=True, blank=True)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='members')


@receiver(pre_save, sender=User)
def create_user_organization(sender, instance, *args, **kwargs):
    organization = Organization.objects.create(
        name=f"{instance.first_name}'s organization"
    )
    instance.organization = organization
