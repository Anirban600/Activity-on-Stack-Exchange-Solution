#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:

    line = line.strip()

    pattern = re.compile(r'CreationDate="[^"]*')
    matches = pattern.finditer(line)
    text = None
    for match in matches: text = match.group(0)
    if not text: continue

    hour = text[25:27]
    
    print(f'{hour}\t1')
