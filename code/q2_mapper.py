#!/usr/bin/env python3

import sys

# read all lines from input file
lines = sys.stdin.readlines()

# loop through lines and print vehicle type tab delimited with 1
for line in lines[1:]:
    print('%s\t%s' % (line.split(",")[14], 1))
