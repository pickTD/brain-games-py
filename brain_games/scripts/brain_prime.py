#!/usr/bin/env python3

"""Brain-prime game entry point."""

from brain_games import engine
from brain_games.games import prime


def main():
    """Brain-prime game entry point."""
    user_name = engine.acquaintance()
    engine.print_instructions(prime.INSTRUCTIONS)
    engine.play(user_name, prime.get_round)


if __name__ == '__main__':
    main()
