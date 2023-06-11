#!/usr/bin/env python3

import sys
# read lines from input
lines = sys.stdin.readlines()

for line in lines[1:]:
    line = line.replace('"','').split(',') #remove "" from lines and split

    # we only need data for 'Car' so check for this value on index 14 of line
    if line[14] == 'CAR':
        # we only need trackers for four junctions so check if index 0 contains those tracker values
        if line[0] == '000000020076' or line[0] == '000000020077' or line[0] == '000000020078' or line[0] == '000000020079':
            #print hour which is index 4 of line
            hour = line[4]
            # just to make it look consistant add 0 if hour length is single digit
            # e.g. 0 will become 00 and 1 will become 01 (helps in sorting)
            if len(hour) < 2:
                hour = '0' + hour
            print(f"{hour}\t1")
