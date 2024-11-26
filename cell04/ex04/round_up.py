#!/usr/bin/env python3
import sys
import math

if len(sys.argv) > 1:
    sys.exit(1)


try:
    num = float(input("Give me a number: "))
    if num.is_integer():
        print(num)
    else:
        num = math.ceil(num)
        print(num)
except  ValueError:
    print("Not a number")
