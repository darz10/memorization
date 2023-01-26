from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from accounts.models import User


def get_auth_token(user: User) -> str:
    """
    Generate authentication token for user
    """
    payload = JSONWebTokenAuthentication.jwt_create_payload(user)
    token = JSONWebTokenAuthentication.jwt_encode_payload(payload)
    return token


def soft_delete_user(user: User) -> None:
    """
    Soft delete user. Change field is_active to False
    """
    user.is_active = False
    user.save()
