"""Brain-calc game resources."""

import random

INSTRUCTIONS = 'What is the result of the expression?'


def get_round():
    """Сreate a question and answer for one stage of game.

    Returns:
        list: Question and correct answer for current round.
    """
    operand_one = random.randint(1, 100)
    operand_two = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    question = '{0} {1} {2}'.format(operand_one, operator, operand_two)
    correct_answer = str(eval(question))

    return [question, correct_answer]
