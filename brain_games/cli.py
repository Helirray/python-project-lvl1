import prompt


def welcome_user():
    your_name = prompt.string('May I have your name? ')
    print(f'Hello, {your_name}')
