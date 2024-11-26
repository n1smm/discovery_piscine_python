#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
    sys.exit(1)

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
except ValueError:
    print("none")
    sys.exit(1)

result = []
for i in range(start, end + 1):
    result.append(i)
print(result)
    
