#!/usr/bin/env python3
import sys
import os

dupont_family = \
{
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
}

def has_red_hair(pair):
    key, value = pair
    if value == "red":
        return True
    else:
        return False

def find_the_redheads(family):
    red_heads = []
    red_heads = filter(has_red_hair, family.items())
    red_heads = dict(red_heads)
    red_heads = list(red_heads.keys())
    return (red_heads)

reds = find_the_redheads(dupont_family)
print(reds)



