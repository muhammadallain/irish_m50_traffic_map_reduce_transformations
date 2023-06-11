#!/usr/bin/env python3

import sys

current_count = 0
current_sum = 0

#calculate sum of speed and total count
for line in sys.stdin:
    line = line.strip()
    total, sum = line.split('\t')
    try:
        total = int(total)
        sum = float(sum)
    except ValueError:
        continue

    current_count += total
    current_sum += sum
average = current_sum/current_count #calculate average
print(f"Average speed of motorbikes: {round(average, 2)}") #print results
