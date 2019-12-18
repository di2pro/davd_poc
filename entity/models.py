from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField


class Entity(models.Model):
    is_enabled = models.BooleanField(default=True, null=False, blank=False)
    name = models.CharField(null=False, blank=False, max_length=120)
    created_at = models.DateTimeField(auto_created=True)
    disabled_at = models.DateTimeField(null=True, blank=True)
    organization = models.ForeignKey('organization.Organization', related_name='entities', on_delete=models.CASCADE)


class EntityData(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    data = JSONField()
    entity = models.ForeignKey('Entity', related_name='data', on_delete=models.CASCADE)
