from rest_framework import serializers

from reminder.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    '''
    Reminder serializer
    '''

    class Meta:
        model = Reminder
        fields = [
            "id",
            "user",
            "text",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "created_at", "user", "status"]

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return super().validate(attrs)
