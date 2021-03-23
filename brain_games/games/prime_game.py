from brain_games.games.engine import is_prime, check_answer
from random import randint


def check_prime(user_name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        num = randint(2, 200)
        print(f'Question: {num}')
        correct_answer = 'yes' if is_prime(num) else 'no'
        answer = input()
        if check_answer(answer, correct_answer, user_name):
            count += 1
        else:
            return
