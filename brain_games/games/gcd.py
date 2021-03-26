from random import randint

START_GAME_MESSAGE = 'Find the greatest common divisor of given numbers.'


def gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    return num_1 + num_2


def generate_game_values():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    return f'{num_1} {num_2}', gcd(num_1, num_2)
