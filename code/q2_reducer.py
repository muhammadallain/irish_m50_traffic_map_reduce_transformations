#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
total = len(lines)
current_word = ""
current_count = 0
word = ""

for line in lines:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{round(current_count/total*100, 2)}%")
        current_count = count
        current_word = word
if current_word == word:
    print(f"{current_word}\t{round(current_count/total*100, 2)}%")
