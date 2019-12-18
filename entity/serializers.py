from rest_framework import serializers

from . import models


class EntityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EntityData
        fields = '__all__'


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entity
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['data'] = EntityDataSerializer(instance.data, many=True, read_only=True).data
        return response
