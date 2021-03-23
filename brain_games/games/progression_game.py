from brain_games.games.engine import generate_progression, check_answer


def check_number_of_progression(user_name):
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        correct_answer = generate_progression()
        answer = input()
        if check_answer(answer, correct_answer, user_name):
            count += 1
        else:
            count = 0
