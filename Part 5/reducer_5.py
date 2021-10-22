#!/usr/bin/env python3

import sys

count = 0
n = 0
sum_x = 0
sum_y = 0
sum_xy = 0
sum_x2 = 0
sum_y2 = 0

for line in sys.stdin:
    line = line.strip()
    
    user_id, mode, val = list(map(int, line.split('\t')))

    if mode == 2:
        print(f'{user_id}\t{count}\t{val}')
        n += 1
        sum_x += count
        sum_y += val
        sum_xy += count * val
        sum_x2 += count ** 2
        sum_y2 += val ** 2
        count = 0
    else:
        count += val

print('Correlation Coefficient is :')
a = n * sum_xy - sum_x * sum_y
b = ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5
print(a / b)
