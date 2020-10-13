#!/usr/bin/env python3

"""Brain-prime game entry point."""

from brain_games import engine
from brain_games.games import prime


def main():
    """Brain-prime game entry point."""
    engine.play(prime.INSTRUCTIONS, prime.get_round)


if __name__ == '__main__':
    main()
