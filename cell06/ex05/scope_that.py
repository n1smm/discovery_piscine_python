#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit(1)

def add_one(num):
    num += num
    return (num)

num = 1
print(num)
add_one(num)
print(num)
num = add_one(num)
print(num)
