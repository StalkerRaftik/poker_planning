from uuid import uuid4


def generate_game_code():
    return uuid4().hex[:6]
