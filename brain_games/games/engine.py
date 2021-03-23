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


def generate_gcd():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    print(f'Question: {num_1} {num_2}')
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    return num_1 + num_2


def check_answer(user_answer, correct_answer, user_name):
    if user_answer == str(correct_answer):
        print(f'Your answer: {user_answer}\nCorrect!')
        return True
    else:
        print(f'Your answer: {user_answer}\n'
              f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.\n"
              f"Let's try again, {user_name}!")
        return False


def generate_progression():
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
    print(f'Question: {progression}')
    return correct_answer


def is_prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def congratulate_user(user_name):
    print(f'Congratulations, {user_name}!')
