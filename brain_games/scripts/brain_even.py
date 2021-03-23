from games.engine import welcome_user_and_get_user_name, congratulate_user
from games.even_game import check_even


def main():
    user_name = welcome_user_and_get_user_name()
    check_even(user_name)
    congratulate_user(user_name)


if __name__ == '__main__':
    main()
