#!/usr/bin/env python3
import sys

if len(sys.argv) < 3:
    print("none")
    sys.exit(1)
result = []
# this pops/removes form the parent list and copies it to new list in reverse order
# result = [sys.argv.pop() for _ in range(len(sys.argv) -1)]

# this pops/remove and copies as is
# result = [sys.argv[i] for i in range(1, len(sys.argv), 1)]

#this slices/copies the list [start,end,step]
result = sys.argv[:0:-1]
 
#could be also (this first copies in order, and after that it reverses it)
# result = sys.argv[1::][::-1]

#reversing also the chars
# result2 = []
# for memb in result:
#     result2.append(memb[::-1])
#or
# for i in range(len(result)):
#     result[i] = result[i][::-1]

print(result)
