from brain_games.games.progression_game\
    import check_number_of_progression
from brain_games.games.engine\
    import welcome_user_and_get_user_name, congratulate_user


def main():
    user_name = welcome_user_and_get_user_name()
    check_number_of_progression(user_name)
    congratulate_user(user_name)


if __name__ == '__main__':
    main()
