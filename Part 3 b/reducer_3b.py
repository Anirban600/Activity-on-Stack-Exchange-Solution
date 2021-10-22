#!/usr/bin/env python3
import os
import sys

cur_view = None
cur_count = 0
view = None
top_10 = []

for line in sys.stdin:
    line = line.strip()

    try:
        view, count, title = line.split('\t')
    except:
        arr = line.split('\t')
        view = arr[0]
        count = arr[1]
        title = ' '.join(arr[2:])
    
    count = int(count)
    view = int(view)

    if len(top_10) < 10:
        top_10.append([view, title])
        top_10.sort()
    elif top_10[-1][0] < view:
        top_10.append([view, title])
        top_10.pop(0)
    
    if cur_view == view: cur_count += count
    else:
        if cur_view:
            print (f'{cur_view}\t{cur_count}')
        cur_count = count
        cur_view = view


if cur_view == view: print (f'{cur_view}\t{cur_count}')


print("\nTop 10 most viewed posts are :\n")
for view, title in reversed(top_10):
    print(view, '\t', title)
