#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    line = line.strip()
    
    pattern = re.compile(r'Tags="[^"]*')
    matches = pattern.finditer(line)
    text = None
    for match in matches: text = match.group(0)

    if not text: continue
    text = text[6:]
    while '&gt;' in text: text = text.replace('&gt;', ' ')
    while '&lt;' in text: text = text.replace('&lt;', ' ')
    for tag in text.split(): print(f'{tag}\t1')
