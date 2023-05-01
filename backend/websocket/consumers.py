import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class GameRoom(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_id = None
        self.room_group_name = None

    def connect(self):
        game_id = self.scope["url_route"]["kwargs"]["game_id"]
        self.connect_game(game_id)

    def connect_game(self, game_id):
        if not True:
            self.accept_connection()
            self.send(text_data=json.dumps({
                'type': 'game_not_found',
                'game_id': game_id,
            }))
            self.break_connection()
            return

        self.game_id = game_id
        self.accept_connection()
        self.send(text_data=json.dumps({
            'type': 'connected_to_game',
            'game_id': self.game_id,
        }))

    def accept_connection(self):
        self.room_group_name = f"game_{self.game_id}"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def break_connection(self):
        self.close()
        if not self.room_group_name:
            return
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from client
    def receive(self, text_data):
        message = json.loads(text_data)
        handler = getattr(self, f'on_{message["type"]}', None)
        if not handler:
            self.send(text_data=json.dumps({
                'type': 'no_such_message',
            }))
        handler(message)

    def dispatch_game_event(self, event_type, data):
        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {
            'type': 'game_event',
            'event_type': event_type,
            'data': data,
        })

    def game_event(self, event):
        """Received 'game_event' data, send to all clients"""
        self.send(text_data=json.dumps(event))
