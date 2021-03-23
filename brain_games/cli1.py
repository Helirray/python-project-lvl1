import prompt
from random import randint


def welcome_user_and_get_user_name():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}')
    return user_name


def is_even(num):
    return num % 2 == 0


def check_even(user_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = input()
        print(f'Your answer: {answer}')
        if is_even(number) and answer == 'yes' or \
                is_even(number) is False and answer == 'no':
            print('Correct!')
            count += 1
        elif is_even(number) and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes' \nLet's try again, {user_name}!")
            count = 0
        elif is_even(number) is False and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no' \nLet's try again, {user_name}!")
            count = 0
    print(f'Congratulations, {user_name}!')

