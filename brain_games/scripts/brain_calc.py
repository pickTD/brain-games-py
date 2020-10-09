#!/usr/bin/env python3

"""Brain-calc game entry point."""

from brain_games import engine
from brain_games.games import calc


def main():
    """Brain-calc game entry point."""
    user_name = engine.acquaintance()
    engine.print_instructions(calc.INSTRUCTIONS)
    engine.play(user_name, calc.get_round)


if __name__ == '__main__':
    main()
