from random import randint, choice

START_GAME_MESSAGE = 'What is the result of the expression?'


def generate_game_values():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    add = (f'{num_1} + {num_2}', num_1 + num_2)
    sub = (f'{num_1} - {num_2}', num_1 - num_2)
    mul = (f'{num_1} * {num_2}', num_1 * num_2)
    return choice(add, sub, mul)
