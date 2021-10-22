#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    line = line.strip()
    
    pattern = re.compile(r'Title="[^"]*')
    matches = pattern.finditer(line)
    title = ''
    for match in matches:
        title = match.group(0)[7:]

    pattern = re.compile(r'ViewCount="[^"]*')
    matches = pattern.finditer(line)
    count = None
    for match in matches:
        count = int(match.group(0)[11:])
    
    if count != None:
        print(f'{count}\t1\t{title}')
