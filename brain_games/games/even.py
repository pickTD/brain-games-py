"""Brain-even game resources."""

import random

INSTRUCTIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    """Сreate a question for one stage of game.

    Returns:
        int: Random number in range 1 - 100.
    """
    return random.randint(1, 100)


def get_answer(question):
    """Сreate a question for one stage of game.

    Args:
        question (int): Number to compare with condition.

    Returns:
        str: Result of comparing number with condition.
    """
    return 'yes' if question % 2 == 0 else 'no'
