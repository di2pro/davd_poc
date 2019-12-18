from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from . import models, serializers


class EntityListViewSet(ListModelMixin, GenericViewSet):
    model = models.Entity
    serializer_class = serializers.EntitySerializer


class EntityDataListViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    model = models.EntityData
    serializer_class = serializers.EntityDataSerializer
