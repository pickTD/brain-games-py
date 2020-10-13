#!/usr/bin/env python3

"""Brain-gcd game entry point."""

from brain_games import engine
from brain_games.games import gcd


def main():
    """Brain-gcd game entry point."""
    engine.play(gcd.INSTRUCTIONS, gcd.get_round)


if __name__ == '__main__':
    main()
