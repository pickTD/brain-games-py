"""Brain-even game implementation."""

import random

import prompt


def acquaintance():
    """Ask for a username and greet him.

    Returns:
        str: User entered name
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name


def print_instructions():
    """Print instructions for game."""
    print('Answer "yes" if the number is even, otherwise answer "no".')


def play(user_name):
    """Start game.

    Args:
        user_name (str): Player name
    """
    answers_count = 0
    goal = 3
    while answers_count < goal:
        question = random.randint(1, 1024)
        correct_answer = 'yes' if question % 2 == 0 else 'no'
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
