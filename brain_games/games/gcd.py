"""Brain-gcd game resources."""

import math
import random

INSTRUCTIONS = 'Find the greatest common divisor of given numbers.'


def get_question():
    """Сreate a question for one stage of game.

    Returns:
        str: Two random numbers in range 1 - 100.
    """
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)

    return '{0} {1}'.format(number_one, number_two)


def get_answer(question):
    """Сreate a question for one stage of game.

    Args:
        question (str): Two numbers divided by whitespace.

    Returns:
        str: Greatest common divisor of given numbers.
    """
    [number_one_str, number_two_str] = question.split(' ')
    gcd = math.gcd(int(number_one_str), int(number_two_str))
    return str(gcd)
