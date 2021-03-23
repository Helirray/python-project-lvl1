from brain_games.games.engine\
    import welcome_user_and_get_user_name, congratulate_user
from brain_games.games.gcd_game import check_gcd


def main():
    user_name = welcome_user_and_get_user_name()
    check_gcd(user_name)
    congratulate_user(user_name)


if __name__ == '__main__':
    main()
