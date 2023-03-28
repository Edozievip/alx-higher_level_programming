#!/usr/bin/python3

def safe_print_integer(value):

	try:
		print("{:d}".format())
		return (true)
	except (TypeError, ValueError):
		return (false)

