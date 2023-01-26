from rest_framework.exceptions import ValidationError


class WrongPasswordError(ValidationError):
    pass
