#!/usr/bin/env python3

"""Application entry point."""

from brain_games import cli


def main():
    """Application entry point (actually)."""
    print('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
