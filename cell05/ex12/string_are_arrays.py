#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
    sys.exit(1)

argu = sys.argv[1]

for char in argu:
    if char == 'z':
        print("z", end='')
print("")
