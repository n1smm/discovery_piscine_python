#!/usr/bin/env python3
import os
import sys

persons = \
{
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
}


def array_of_names(persons):
    full_names = []
    for first, second in persons.items():
        full_names.append(first.capitalize() + " " + second.capitalize())
    return (full_names)

full_names = array_of_names(persons)
print(full_names)
