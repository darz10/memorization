# chat/consumers.py

import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import channels.layers


class ReminderStatusConsumer(WebsocketConsumer):
    """

    """

    def connect(self):
        user = self.scope.get('user', None)
        self.channel_layer = channels.layers.get_channel_layer()
        if not user.id:
            self.room_group_name = 'error_channel'
        else:
            self.user = user
            self.room_group_name = 'user_%s' % self.user.id
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
        self.accept()
        if not user.id:
            self.send(text_data=json.dumps({
                'error': '401',
                'message': 'Websockets are only available to authorized users'
            }))
            self.close()
            return

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        if text_data == 'ping':
            self.send(text_data=json.dumps({
                'event_type': 'pong',
                'message': 'pong'
            }))

    def reminder_notification(self, event):
        message = event['message']
        data = {'type': 'reminder_notification', 'data': message}
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': data
        }))


def reminder_notification_message(user_id: int, event_data):
    """
    Function for send data notification by websocket
    """
    group_name = f'user_{user_id}'
    data = {
        'type': 'reminder_notification',
        'message': event_data
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(group_name, data)
