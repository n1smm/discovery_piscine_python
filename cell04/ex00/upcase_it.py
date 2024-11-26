#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    sys.exit(1);

input = input("give me a word: ")
up_case = input.upper()
print (up_case)
