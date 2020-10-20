"""Brain-calc game resources."""

import random

from brain_games import engine

INSTRUCTIONS = 'What is the result of the expression?'


def calculate(operand_one, operand_two, operator):
    """Сreate a question and answer for one stage of game.

    Args:
        operand_one (int): First operand of expression.
        operand_two (int): Second operand of expression.
        operator (str): String representation of a mathematical operator.

    Raises:
        ValueError: If operator is unknown

    Returns:
        int: Evaluated expression.
    """
    if operator == '+':
        calculation = operand_one + operand_two
    elif operator == '-':
        calculation = operand_one - operand_two
    elif operator == '*':
        calculation = operand_one * operand_two
    else:
        raise ValueError('Unknown operator:', operator)
    return calculation


def get_round():
    """Сreate a question and answer for one stage of game.

    Returns:
        tuple: Question and correct answer for current round.
    """
    operand_one = random.randint(1, 100)
    operand_two = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    question = '{0} {1} {2}'.format(operand_one, operator, operand_two)
    correct_answer = str(calculate(operand_one, operand_two, operator))

    return question, correct_answer


def play():
    """Start the game."""
    engine.play(INSTRUCTIONS, get_round)
