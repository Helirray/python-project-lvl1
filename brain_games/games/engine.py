import prompt
from random import randint, choice


def welcome_user_and_get_user_name():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}')
    return user_name


def is_even(num):
    return num % 2 == 0


def calculate_random_numbers():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    expression = choice((num_1 + num_2, num_1 * num_2, num_1 - num_2))
    if expression == num_1 + num_2:
        print(f'Question: {num_1} + {num_2}')
    elif expression == num_1 * num_2:
        print(f'Question: {num_1} * {num_2}')
    elif expression == num_1 - num_2:
        print(f'Question: {num_1} - {num_2}')
    return expression


def congratulate_user(user_name):
    print(f'Congratulations, {user_name}!')
