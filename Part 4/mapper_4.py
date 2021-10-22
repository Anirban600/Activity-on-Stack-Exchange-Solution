#!/usr/bin/env python3

import sys
import re
import datetime

start = datetime.datetime(2014, 5, 1)
end = datetime.datetime(2021, 9, 30)

for line in sys.stdin:

    line = line.strip()
    
    pattern = re.compile(r'Text="[^"]*')
    matches = pattern.finditer(line)
    comment = ''
    for match in matches:
        comment = match.group(0)[6:]

    pattern = re.compile(r'CreationDate="[^"]*')
    matches = pattern.finditer(line)
    time = None
    for match in matches:
        time = match.group(0)

    if not time: continue
    
    year = int(time[14:18])
    month = int(time[19:21])
    day = int(time[22:24])
    curr = datetime.datetime(year, month, day)
    
    if start <= curr <= end:
        print(f'{time[14:21]}\t1\t{len(comment)}')
