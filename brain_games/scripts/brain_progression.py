#!/usr/bin/env python3

"""Brain-progression game entry point."""

from brain_games import engine
from brain_games.games import progression


def main():
    """Brain-progression game entry point."""
    user_name = engine.acquaintance()
    engine.print_instructions(progression.INSTRUCTIONS)
    engine.play(user_name, progression.get_round)


if __name__ == '__main__':
    main()
