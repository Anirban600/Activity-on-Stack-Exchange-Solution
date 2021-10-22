#!/usr/bin/env python3

import sys
from datetime import date

time = date(2021, 9, 30) - date(2014, 5, 1)
days = time.days

cur_hour = None
cur_count = 0
hour = None
track = []

print("Here, no of days = May-2014 to Sept-2021 =", days, end='\n\n')
print(f'Hour\tTotal Posts\tPosts per Day')
for line in sys.stdin:
    line = line.strip()
    
    hour, count = line.split('\t')
    count = int(count)
    
    if cur_hour == hour:
        cur_count += count
    else:
        if cur_hour:
            print(f'{cur_hour}\t{cur_count}\t\t{cur_count/days}')
            track.append([cur_count/days, cur_hour])
        cur_hour = hour
        cur_count = count

if cur_hour == hour:
    print(f'{cur_hour}\t{cur_count}\t\t{cur_count/days}')
    track.append([cur_count/days, cur_hour])

track.sort()
print("Max posts :", track[-1][0], "at", track[-1][1], "houre")
print("Min posts :", track[0][0], "at", track[0][1], "houre")

print("Ratio :", track[-1][0] / track[0][0])
