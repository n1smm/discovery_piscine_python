#!/usr/bin/env python3
import sys

def greetings(name=None):
    try:
        if name is None:
            print("Hello, noble stranger.")
        elif not isinstance(name, str):
            raise TypeError("Argument is not a string")
        else:
            print("hello,", name + ".")
    except TypeError as e:
        print(e)

greetings("gugi")
greetings("midori")
greetings()
greetings(int(1234))
