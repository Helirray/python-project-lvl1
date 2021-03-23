import prompt
from random import randint


def welcome_user_and_get_user_name():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}')
    return user_name


def is_even(num):
    return num % 2 == 0


def congratulate_user(user_name):
    print(f'Congratulations, {user_name}!')
