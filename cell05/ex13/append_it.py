#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
    sys.exit(1)

for memb in sys.argv[1::]:
    if not memb.endswith("ism"):
        print(memb + "ism")
