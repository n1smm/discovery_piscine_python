#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    sys.exit(1)

try:
    word = input()
    output = ""
    fast = ''.join([char.upper() if char.islower() else char.lower() for char in word])
    for char in word:
        if char.islower() == True:
            output += char.upper()
        else:
            output += char.lower()
    print(output);
    print(fast);
except ValueError:
    print("upsi")
            
