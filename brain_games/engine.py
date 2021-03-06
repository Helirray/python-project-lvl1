import prompt

NUMBER_OF_ROUNDS = 3


def execute(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}')
    print(game.START_GAME_MESSAGE)
    rounds_count = 0
    while rounds_count < NUMBER_OF_ROUNDS:
        question, correct_answer = game.generate_game_values()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
            rounds_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
