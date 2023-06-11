#!/usr/bin/env python3

import sys

word = ''
max_count = 0
max_word = ''
min_count = 10 * 100
min_word = ''
hour_dict = {}

#read lines from input
for line in sys.stdin:
    line = line.strip()
    try:
        hour, count = line.split('\t')
    except ValueError:
        continue
    try:
        count = int(count)
    except ValueError:
        continue
    #if key is not in dictionary than add the key in dictionary
    if hour not in hour_dict:
        hour_dict[hour] = 1
    #otherwise increase the count for that key
    else:
        hour_dict[hour] += count
#loop through dictionary to check for minimum and maximum values
for hour in hour_dict:
    if hour_dict[hour] > max_count:
        max_count = hour_dict[hour]
        max_word = hour
    if hour_dict[hour] < min_count:
        min_count = hour_dict[hour]
        min_word = hour
#print those minimum and maximum values
print(f"Hour with highest flows for Cars: {max_word}:00 - {max_word}:59\t{max_count}")
print(f"Hour with lowest flows for Cars: {min_word}:00 - {min_word}:59\t{min_count}")
