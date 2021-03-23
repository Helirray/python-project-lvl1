from brain_games.games.engine import generate_gcd, check_answer


def check_gcd(user_name):
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        correct_answer = generate_gcd()
        answer = input()
        if check_answer(answer, correct_answer, user_name):
            count += 1
        else:
            count = 0
