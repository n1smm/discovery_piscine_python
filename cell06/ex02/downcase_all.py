#!/usr/bin/env python3
import sys

def downcase_it(word):
    word = word.lower()
    return (word)

if len(sys.argv) < 2:
    print("none")
    sys.exit(1)

for memb in sys.argv[1::]:
    memb = downcase_it(memb)
    print(memb)
