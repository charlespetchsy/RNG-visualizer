#!/usr/bin/env python

import random
SIZE = 100000
aList = []
for i in range(SIZE):
    getNum = random.randint(0,9)
    aList.append(getNum)

print([[x, (aList.count(x) / SIZE)] for x in set(aList)])