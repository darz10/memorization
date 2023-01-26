from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class EmailBackend(ModelBackend):
    '''
    Класс для реализации авторизации по почте
    '''
    def authenticate(self, request, username=None, password=None, **kwargs):
        params = Q(username=username) | Q(email=username)
        user_model = get_user_model()
        try:
            user = user_model.objects.get(params)
        except user_model.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
