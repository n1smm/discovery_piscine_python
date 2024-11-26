#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
    sys.exit(1)
print(sys.argv.pop(1))
