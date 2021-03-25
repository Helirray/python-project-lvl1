from random import randint, choice

START_GAME_MESSAGE = 'What is the result of the expression?'


def generate_game_values():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    expression = choice((num_1 + num_2, num_1 * num_2, num_1 - num_2))
    if expression == num_1 + num_2:
        return f'{num_1} + {num_2}', expression
    elif expression == num_1 * num_2:
        return f'{num_1} * {num_2}', expression
    elif expression == num_1 - num_2:
        return f'{num_1} - {num_2}', expression
