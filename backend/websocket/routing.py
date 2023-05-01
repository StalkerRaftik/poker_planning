from django.urls import re_path

from websocket import consumers

websocket_urlpatterns = [
    re_path(r"ws/game_room/(?P<game_id>\w*)/$", consumers.GameRoom.as_asgi()),
]
