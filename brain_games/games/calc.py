"""Brain-calc game resources."""

import random

INSTRUCTIONS = 'What is the result of the expression?'


def get_question():
    """Сreate a question for one stage of game.

    Returns:
        str: Mathematical expression.
    """
    operand_one = random.randint(1, 100)
    operand_two = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    return '{0} {1} {2}'.format(operand_one, operator, operand_two)


def get_answer(question):
    """Сreate a question for one stage of game.

    Args:
        question (str): Mathematical expression.

    Returns:
        str: Result of evaluating an expression.
    """
    return str(eval(question))
