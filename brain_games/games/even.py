from random import randint

START_GAME_MESSAGE = 'What is the result of the expression?\n' \
                     'Answer "yes" if the number is even,' \
                     ' otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def generate_game_values():
    number = randint(1, 100)
    return number, 'yes' if is_even(number) else 'no'
