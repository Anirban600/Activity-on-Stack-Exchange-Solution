#!/usr/bin/env python3

import sys

cur_tag = None
cur_count = 0
tag = None

for line in sys.stdin:
    line = line.strip()
    
    tag, count = line.split('\t')
    count = int(count)
    
    if cur_tag == tag: cur_count += count
    else:
        if cur_tag:
            print(f'{cur_tag}\t{cur_count}')
        cur_count = count
        cur_tag = tag

if cur_tag == tag:
    print(f'{cur_tag}\t{cur_count}')
