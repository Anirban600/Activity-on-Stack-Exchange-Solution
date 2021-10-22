#!/usr/bin/env python3

import sys
from matplotlib import pyplot as plt

data = []

for line in sys.stdin:
    line = line.strip()
    tag, count = line.split()
    data.append(int(count))
    data.sort()

plt.title('Tag Popularity Distribution')
plt.xlabel('Count per Tag')
plt.ylabel('Popularity')
plt.hist(data, bins=200)
plt.savefig('Distribution_3a.png')
