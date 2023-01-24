import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there! Nice to meet you.'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == 'roll20':
        return str(random.randint(1, 20))

    if p_message == 'help':
        return "Can't help you :("
    