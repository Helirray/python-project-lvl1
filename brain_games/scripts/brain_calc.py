from brain_games.games.calc_game\
    import check_calculatings
from brain_games.games.engine\
    import congratulate_user, welcome_user_and_get_user_name


def main():
    user_name = welcome_user_and_get_user_name()
    check_calculatings(user_name)


if __name__ == '__main__':
    main()
