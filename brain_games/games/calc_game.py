from brain_games.games.engine \
    import calculate_random_numbers, congratulate_user, check_answer


def check_calculatings(user_name):
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        correct_answer = calculate_random_numbers()
        answer = input()
        if check_answer(answer, correct_answer, user_name):
            count += 1
        else:
            return
    congratulate_user(user_name)
