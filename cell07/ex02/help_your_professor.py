#!/usr/bin/env python3
import sys
import os

class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
}
class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
}

def average(school_class):
    average_score = 0
    i = 0
    for name, score in school_class.items():
        average_score += score
        i += 1
    average_score /= i
    return (average_score)

print(average(class_3B))
print(average(class_3C))
