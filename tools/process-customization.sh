#!/usr/bin/env bash
# SPDX-FileCopyrightText: Copyright (c) 2021 Hugo Dahl
# SPDX-FileCopyrightText: 2021 & CircuitPython contributors (https://github.com/adafruit/circuitpython/graphs/contributors)
#
# SPDX-License-Identifier: MIT

pip install -r ./requirements-customization.txt

./process_customization.py
