from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from reminder.tasks import notification_reminders

from rest.serializers import ReminderSerializer
from reminder.models import Reminder


tags = ['reminder']


@method_decorator(
    swagger_auto_schema(
        operation_id='Get list reminders',
        tags=tags,
    ), 'list')
@method_decorator(
    swagger_auto_schema(
        operation_id='Create reminder',
        tags=tags,
    ), 'create')
@method_decorator(
    swagger_auto_schema(
        operation_id='Get reminder',
        tags=tags,
    ), 'retrieve')
@method_decorator(
    swagger_auto_schema(
        operation_id='Update reminder',
        tags=tags,
    ), 'update')
@method_decorator(
    swagger_auto_schema(
        operation_id='Partly update reminder',
        tags=tags,
    ), 'partial_update')
@method_decorator(
    swagger_auto_schema(
        operation_id='Delete reminder',
        tags=tags,
    ), 'destroy')
class ReminderViewSet(ModelViewSet):
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        self.queryset = Reminder.objects.user_own_reminders(user)
        notification_reminders()
        return super().list(request, *args, **kwargs)
