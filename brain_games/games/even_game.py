from brain_games.games.engine import is_even, check_answer
from random import randint


def check_even(user_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = input()
        correct_answer = 'yes' if is_even(number) else 'no'
        if check_answer(answer, correct_answer, user_name):
            count += 1
        else:
            count = 0
