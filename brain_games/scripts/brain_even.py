#!/usr/bin/env python3

"""Brain-even game entry point."""

from brain_games import even


def main():
    """Brain-even game entry point."""
    user_name = even.acquaintance()
    even.print_instructions()
    even.play(user_name)


if __name__ == '__main__':
    main()
