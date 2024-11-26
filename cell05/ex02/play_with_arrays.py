#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    sys.exit(1)

initial = [2,4,5,6,23,9]
result = [integer + 2 for integer in initial if  integer > 5]
print(result)
