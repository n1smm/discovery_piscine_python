#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
    sys.exit(1)

def shrink(word):
    word = word[:8:]
    return (word)
def enlarge(word):
    word += 'Z' * (8 - len(word))
    return (word)

args = sys.argv[1::]
for i in range(len(args)):
    if len(args[i]) < 8:
        args[i] = enlarge(args[i])
    elif len(args[i]) > 8:
        args[i] = shrink(args[i])
print(args)
