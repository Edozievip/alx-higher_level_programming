#!/usr/bin/python3
"""
Defines MyList class
"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints the list in sorted ascending order."""
        print(sorted(self))
