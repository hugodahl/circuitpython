#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2021 Hugo Dahl
# SPDX-FileCopyrightText: 2021 & CircuitPython contributors (https://github.com/adafruit/circuitpython/graphs/contributors)
#
# SPDX-License-Identifier: MIT

import os, sys
from jinja2 import Environment, Template
from pathlib import Path

from customization_config import config

def print_vals(val, depth = 0):
	if type(val) is dict:
		for k in val:
			print("  " * depth, k)
			print_vals(val[k], depth + 1)
	else:
		if val[:-1] == "$":
			print(os.env(val[1:]))
		else:
			print("  " * depth, " ", val)

def print_filesets(filesets):
	for fileset in filesets:
		if fileset[0] == '/':
			fileset = '.' + fileset
		print_fileset_matches(fileset)


def print_fileset_matches(pattern):
	print(f"Processing pattern {pattern} . . .")
	path = Path('.')
	matches = path.glob(pattern)
	for match in matches:
		print(match)

def print_help():
	print("""This tool processes a configuration file, 'customization_config.py', for file paths
	to perform string replacements in the given patterns. The paths are relative to the location
	from which the script is called, or `$PWD`.""")

# Check to see if help has been requested
if '-h' in sys.argv:
	print_help()
	exit()


print_vals(config)

filesets = config['fileset']
print_filesets(filesets)
