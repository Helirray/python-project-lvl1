from random import randint

START_GAME_MESSAGE = 'What number is missing in the progression?'


def generate_game_values():
    start = randint(1, 100)
    step = randint(2, 10)
    length = randint(5, 10)
    progression = [start] + [0] * (length - 1)
    for i in range(1, length):
        progression[i] = progression[i - 1] + step
    deleted_digit_number = randint(0, len(progression) - 1)
    correct_answer = progression[deleted_digit_number]
    progression[deleted_digit_number] = '..'
    progression = ' '.join(map(str, progression))
    return f'Question: {progression}', correct_answer
