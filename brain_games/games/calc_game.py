from brain_games.games.engine import calculate_random_numbers, congratulate_user


def check_calculatings(user_name):
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        correct_answer = calculate_random_numbers()
        answer = input()
        if answer == str(correct_answer):
            print(f'Your answer: {answer}\nCorrect!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    congratulate_user(user_name)
