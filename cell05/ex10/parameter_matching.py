#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
    sys.exit(1)

parameter = sys.argv[1]
word = input("What was the parameter? ")
if word == parameter:
    print("Good job!")
else:
    print("Nope, sorry...")
