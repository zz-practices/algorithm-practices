#!/usr/bin/python

import random

def countingSort(data, max_value):
    book = [0 for i in xrange(max_value+1)]
    result = []
    for i in data:
        book[i]+=1
    for i in range(max_value):
        val = book[i]
        for j in range(val):
            result.append(i)
    return result

if __name__=='__main__':
    max_value = 50
    cnt_value = 20
    data = [random.randint(0, max_value) for i in xrange(cnt_value)]
    print data
    print countingSort(data, max_value)
