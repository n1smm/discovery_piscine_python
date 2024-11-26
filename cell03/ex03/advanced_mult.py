#!/usr/bin/env python3
import sys
import os

if (len(sys.argv)) > 1:
    print("none")
    sys.exit(os.EX_SOFTWARE);

for number in range(11):
    print("table of", f"{number:2}", ": ", end="")
    for mult in range (11):
        res = number * mult
        print(f"{res:<3}", end=" ")
    print("")
        
