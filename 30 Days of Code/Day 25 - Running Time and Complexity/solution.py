#!/usr/local/bin/python3

"""Task 

A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
Given a number, n, determine and print whether it's Prime or Not prime.

Note: If possible, try to come up with a O(sqrt(n)) primality algorithm, or see what sort of optimizations you come up with for an O(n) algorithm. 
Be sure to check out the Editorial after submitting your code!
"""

import math

T=int(input())
head=None
n = []
for i in range(T):
    n.append(int(input()))
    
for value in n:
    if value == 1:
        print('Not prime')
    else: 
        result = math.ceil(math.sqrt(value))
        find = False
        for r in range(2, result+1):
            if value != r and value % r == 0:
                print('Not prime')
                find = True
                break
        
        if not find:
            print('Prime')
