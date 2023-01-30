from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import (
    GenericViewSet
)
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from accounts.services.users import soft_delete_user

from rest.serializers import (
    UserSerializer,
    AuthorizationUserSerializer,
    JSONTokenSerializer
)
from accounts.models import User


tags = ['users']


@method_decorator(
    swagger_auto_schema(
        operation_id='Create user',
        tags=tags,
    ), 'create')
@method_decorator(
    swagger_auto_schema(
        operation_id='Get user',
        tags=tags,
    ), 'retrieve')
@method_decorator(
    swagger_auto_schema(
        operation_id='Update user',
        tags=tags,
    ), 'update')
@method_decorator(
    swagger_auto_schema(
        operation_id='Partly update user',
        tags=tags,
    ), 'partial_update')
@method_decorator(
    swagger_auto_schema(
        operation_id='Delete user',
        tags=tags,
    ), 'destroy')
class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["create", "authorize"]:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        soft_delete_user(user)
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id='Authorization',
        operation_description='Get authorization token for application',
        request_body=AuthorizationUserSerializer,
        responses={200: JSONTokenSerializer}
    )
    @action(
        detail=False,
        methods=['POST'],
        serializer_class=AuthorizationUserSerializer
    )
    def authorize(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.auth()
        return Response(JSONTokenSerializer({"token": token}).data)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        soft_delete_user(user)
        return Response()
