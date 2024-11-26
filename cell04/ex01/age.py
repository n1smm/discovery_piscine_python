#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    sys.exit(1);
try:
    u_input = int(input("Please tell me your age: "))
    index = 10
    print("You are currently", u_input, "old.")
    while index <= 30:
        print("in 10 years you'll be", u_input + index, "years old")
        index += 10
except ValueError:
    print("Error, input not int")

