from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    '''
    User serializer
    '''

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
        ]
