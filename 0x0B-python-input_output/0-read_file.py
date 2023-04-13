#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """This function reads a UTF8 text file prints it to the stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
