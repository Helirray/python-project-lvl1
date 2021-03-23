from brain_games.cli1 import welcome_user_and_get_user_name, check_even


def main():
    user_name = welcome_user_and_get_user_name()
    check_even(user_name)


if __name__ == '__main__':
    main()
