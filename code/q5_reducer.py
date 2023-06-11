#!/usr/bin/env python3

import sys

current_word = ''
current_count = 0
word = ''
# create empty dictionary
loc = {}
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    # create a new key if its not in dictionary
    if word not in loc:
        loc[word] = 1
    # otherwise increase count of key
    else:
        loc[word] += count
# sort dictionary based on values of keys in descending order
sorted_dict = sorted(loc.items(), key=lambda x:x[1], reverse=True)
#print only top 10 results using for loop
print('Location\tHGV_Counts')
print('------------\t----------')
for key, value in sorted_dict[:10]:
    print(f"{key}\t{value}")
