"""Brain-progression game resources."""

import random

INSTRUCTIONS = 'What number is missing in the progression?'
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10


def get_progression():
    """Create arithmetic progression.

    Returns:
        list: Arithmetic progression.
    """
    progression_length = random.randint(
        MIN_PROGRESSION_LENGTH,
        MAX_PROGRESSION_LENGTH,
    )
    start_point = random.randint(1, 100)
    increment = random.randint(1, 100)
    progression = []
    current_element = start_point
    while len(progression) < progression_length:
        progression.append(current_element)
        current_element += increment

    return progression


def get_round():
    """Сreate a question and answer for one stage of game.

    Returns:
        tuple: Question and correct answer for current round.
    """
    progression = get_progression()
    hidden_element_position = random.randint(0, len(progression) - 1)
    hidden_element = progression[hidden_element_position]
    correct_answer = str(hidden_element)
    progression[hidden_element_position] = '..'
    question = ' '.join(map(str, progression))

    return question, correct_answer
