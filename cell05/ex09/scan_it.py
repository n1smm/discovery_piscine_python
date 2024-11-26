#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
    sys.exit(1)

res = re.findall(sys.argv[1], sys.argv[2])
print(len(res))


