#!/usr/bin/python

import random

MAX=100

data = []
book = []

for i in range(MAX):
    book.append(0)

for i in range(10):
    rand = int(random.random()*1000%MAX)
    data.append(rand)

print data


for i in data:
    book[i] = book[i] + 1

result = []
for i in range(100):
    val = book[i]
    for j in range(val):
        result.append(i)

print result
