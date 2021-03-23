from brain_games.games.engine import is_even
from random import randint


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
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes' \n"
                  f"Let's try again, {user_name}!")
            count = 0
        elif is_even(number) is False and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no' \n"
                  f"Let's try again, {user_name}!")
            count = 0
