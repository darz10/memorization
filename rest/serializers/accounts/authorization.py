from rest_framework import serializers
from accounts.exceptions import WrongPasswordError

from accounts.models.user import User
from rest.messages import EMAIL_USER_NOT_EXISTS, WRONG_PASSWORD
from accounts.services import get_auth_token


class AuthorizationUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        fields = [
            "email",
            "password"
        ]

    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs.get("email"))
            if user.check_password(attrs.get("password")):
                attrs['user'] = user
            else:
                raise WrongPasswordError(WRONG_PASSWORD)
        except User.DoesNotExist:
            raise serializers.ValidationError(EMAIL_USER_NOT_EXISTS)
        return attrs

    def auth(self):
        '''
        Get token for authorization inside the application
        '''
        return get_auth_token(self.validated_data['user'])
