"""Games engine."""

import prompt

GOAL = 3


def acquaintance():
    """Ask for a username and greet him.

    Returns:
        str: User entered name.
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name


def print_instructions(instructions):
    """Print instructions for game.

    Args:
        instructions (str): Instructions for game.
    """
    print(instructions)


def play(user_name, get_round):
    """Start game.

    Args:
        user_name (str): Player name.
        get_round (function): Function returning a question and correct answer.
    """
    answers_count = 0
    while answers_count < GOAL:
        [question, correct_answer] = get_round()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            answers_count += 1
        else:
            print((
                "'{0}' is wrong answer ;(. Correct answer was '{1}'."
                ).format(answer, correct_answer),
            )
            print("Let's try again, {0}!".format(user_name))
            break
    else:
        print('Congratulations, {0}!'.format(user_name))
