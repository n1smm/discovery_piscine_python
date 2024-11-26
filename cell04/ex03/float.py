#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    sys.exit(1)

try:
    num = float(input("Give me a number: "))
    if num.is_integer():
        print("This number is an integer")
    else:
        print("This number is a decimal")
except ValueError:
              print("not a number")
