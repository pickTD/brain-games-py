"""Brain-prime game resources."""

import math
import random

INSTRUCTIONS = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Determine if a number is prime.

    Args:
        number (int): Explored number.

    Returns:
        bool: Is number prime?
    """
    if number < 2:
        return False
    if number < 4:
        return True
    divider = 2
    while divider <= math.sqrt(number):
        remainder = number % divider
        if remainder == 0:
            return False
        else:
            divider += 1
    return True


def get_round():
    """Сreate a question and answer for one stage of game.

    Returns:
        tuple: Question and correct answer for current round.
    """
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer
