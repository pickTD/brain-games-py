#!/usr/bin/env python3

"""Brain-calc game entry point."""

from brain_games import engine
from brain_games.games import calc


def main():
    """Brain-calc game entry point."""
    engine.play(calc.INSTRUCTIONS, calc.get_round)


if __name__ == '__main__':
    main()
