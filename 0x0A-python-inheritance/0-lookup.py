#!/usr/bin/python3
"""Defines an object lookup function."""


def lookup(obj):
    """This function returns the list of available attributes and method of an object"""
    return (dir(obj))
