#!/usr/bin/env python3
import sys

length = len(sys.argv) - 1
print("parameters:", length)
args = sys.argv[1::]
for memb in args:
    print(memb, ":", len(memb))
