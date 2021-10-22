#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:

    line = line.strip()

    if 'PostHistoryTypeId' in line:
        pattern = re.compile(r'PostHistoryTypeId="[^"]*')
        matches = pattern.finditer(line)
        post_type = None
        for match in matches:
            post_type = int(match.group(0)[19:])
        
        pattern = re.compile(r'\sUserId="[^"]*')
        matches = pattern.finditer(line)
        posthist_user_id = None
        for match in matches:
            posthist_user_id = int(match.group(0)[9:])
        
        if post_type == 2 and posthist_user_id:
            print(f'{posthist_user_id}\t1\t1')
    else:
        pattern = re.compile(r'\sId="[^"]*')
        matches = pattern.finditer(line)
        user_id = None
        for match in matches:
            user_id = int(match.group(0)[5:])

        pattern = re.compile(r'Reputation="[^"]*')
        matches = pattern.finditer(line)
        reputation = None
        for match in matches:
            reputation = int(match.group(0)[12:])
        if user_id and reputation:
            print(f'{user_id}\t2\t{reputation}')
