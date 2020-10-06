"""User interaction via the command line."""

import prompt


def welcome_user():
    """Asks for a username and greets him."""
    user_name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=user_name))
