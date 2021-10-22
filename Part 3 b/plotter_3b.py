#!/usr/bin/env python3

import sys
from matplotlib import pyplot as plt

d = dict()

view, count = [], []

for line in sys.stdin:
    line = line.strip()
    arr = line.split()
    if len(arr) == 2: d[int(arr[0])] = int(arr[1])
    else: continue

for v in reversed(sorted(d.keys())):
    view.append(v)
    count.append(d[v])

plt.title('View-Count Distribution')
plt.xlabel('Views')
plt.ylabel('Count per View')
plt.plot(view, count)
plt.savefig('Distribution_3b.png')
