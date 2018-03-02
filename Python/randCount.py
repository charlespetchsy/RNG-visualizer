#!/usr/bin/env python

import random

def pythonRNG(n):

    n = 100000
    aList = []
    for i in range(n):
        getNum = random.randint(0,9)
        aList.append(getNum)

    return ([[x, (aList.count(x) / n)] for x in set(aList)])

def ogRNG(n):
    return None


if __name__ == "__main__":

    print ("Python's built-in RNG (import random):")
    for pair in pythonRNG(1000000000):
        print (pair)