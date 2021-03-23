from brain_games.games.prime_game\
    import check_prime
from brain_games.games.engine\
    import welcome_user_and_get_user_name, congratulate_user


def main():
    user_name = welcome_user_and_get_user_name()
    check_prime(user_name)
    congratulate_user(user_name)


if __name__ == '__main__':
    main()
