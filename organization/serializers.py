from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'created_at',
            'is_enabled',
            'disabled_at',
            'organization',
        )


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['members'] = UserSerializer(instance.members, many=True, read_only=True).data
        return response
