#!/usr/bin/env python3

"""Brain-even game entry point."""

from brain_games import engine
from brain_games.games import even


def main():
    """Brain-even game entry point."""
    user_name = engine.acquaintance()
    engine.print_instructions(even.INSTRUCTIONS)
    engine.play(user_name, even.get_round)


if __name__ == '__main__':
    main()
