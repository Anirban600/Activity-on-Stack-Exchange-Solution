#!/usr/bin/env python3

import sys


def date_formatter(s):
    m = {1 : 'January', 2 : 'February',
         3 : 'March',   4 : 'April',
         5 : 'May',     6 : 'June',
         7 : 'July',    8 : 'August',
         9 : 'September',10 : 'October',
         11 : 'November',12 : 'December'}
    year = s[:4]
    month = m[int(s[5:])]
    return month + ' ' + year


def calc_med(l):
    l.sort()
    if len(l) % 2: return l[len(l) // 2]
    else: return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2


cur_date = None
cur_count = 0
cur_len = []
date = None



for line in sys.stdin:
    line = line.strip()
    
    date, count, length = line.split('\t')
    
    count = int(count)
    length = int(length)
    
    if cur_date == date: 
        cur_count += count
        cur_len.append(length)
    else:
        if cur_date:
            print(f'{date_formatter(cur_date)}\t{cur_count}\t{calc_med(cur_len)}')
        cur_count = count
        cur_date = date
        cur_len = [length]


if cur_date == date: print(f'{date_formatter(cur_date)}\t{cur_count}\t{calc_med(cur_len)}')
