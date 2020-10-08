#!/usr/bin/env python3

"""Brain-gcd game entry point."""

from brain_games import engine
from brain_games.games import gcd


def main():
    """Brain-gcd game entry point."""
    user_name = engine.acquaintance()
    engine.print_instructions(gcd.INSTRUCTIONS)
    engine.play(user_name, gcd.get_question, gcd.get_answer)


if __name__ == '__main__':
    main()
