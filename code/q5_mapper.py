#!/usr/bin/env python3

import sys
#read lines and save in variable
lines = sys.stdin.readlines()

# loop through variable - ignoring first line as header
for line in lines[1:]:
    line = line.replace('"','').split(',')
    #we only need data for HGVs so we look HGV in index 14
    if 'HGV' in line[14]:
        #we only need location data so we print the cosit i.e. index 0 
        print(f"{line[0]}\t1")
