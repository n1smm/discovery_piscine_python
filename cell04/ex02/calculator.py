#!/usr/bin/env python3
import sys
import operator

operations = \
{
        "+" : operator.add,
        "-" : operator.sub,
        "/" : operator.truediv,
        "*" : operator.mul
}
 
if len(sys.argv) > 1:
    sys.exit(1)

try:
    first = int(input("Give me the first number: "))
    second = int(input("Give me the second number: "))
    print("Thank you!")
    for symbol, funct in operations.items():
        res = funct(first, second)
        print("{} {} {} = {}".format(first, symbol, second, res))

except ValueError:
    print("Your input not an int!")
