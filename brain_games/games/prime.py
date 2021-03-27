from random import randint

START_GAME_MESSAGE = (
    'Answer "yes" if given number is prime.'
    ' Otherwise answer "no".'
)


def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i < num / 2:
        if num % i == 0:
            return False
        i += 1
    return True


def generate_game_values():
    num = randint(2, 200)
    return num, 'yes' if is_prime(num) else 'no'
