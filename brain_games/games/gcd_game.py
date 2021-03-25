from random import randint
from copy import copy

START_GAME_MESSAGE = 'Find the greatest common divisor of given numbers.'


def generate_game_values():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    num_3 = copy(num_1)
    num_4 = copy(num_2)
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    return f'{num_3} {num_4}', num_1 + num_2
