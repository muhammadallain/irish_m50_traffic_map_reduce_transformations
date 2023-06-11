#!/usr/bin/env python3

import sys
# read lines and save in variable
lines = sys.stdin.readlines()
# loop through line - ignore first line as header
for line in lines[1:]:
    line = line.replace('"','').split(',')
    # we only need data for motorbikes so we look for 'MBIKE' on index 14
    if line[14] == 'MBIKE':
        # we print the 1 \t 'speed' which is at index 18 
        print(f"1\t{line[18]}")
