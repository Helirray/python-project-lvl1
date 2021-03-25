import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}')
    print(game.START_GAME_MESSAGE)
    rounds_count = 0
    while rounds_count < 3:
        question, correct_answer = game.generate_game_values()
        print(f'Question: {question}')
        user_answer = input()
        if user_answer == str(correct_answer):
            print(f'Your answer: {user_answer}\nCorrect!')
            rounds_count += 1
        else:
            print(f'Your answer: {user_answer}\n'
                  f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
