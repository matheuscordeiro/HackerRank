#!/usr/local/bin/python3

"""Task 

A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
Given a number, n, determine and print whether it's Prime or Not prime.

Note: If possible, try to come up with a O(sqrt(n)) primality algorithm, or see what sort of optimizations you come up with for an O(n) algorithm. 
Be sure to check out the Editorial after submitting your code!
"""

import datetime
return_date=list(map(int, input().rstrip().split()))
expected_date=list(map(int, input().rstrip().split()))
return_date=datetime.date(day=return_date[0], month=return_date[1], year=return_date[2])
expected_date=datetime.date(day=expected_date[0], month=expected_date[1], year=expected_date[2])

if return_date < expected_date:
    print('0')
elif return_date.year > expected_date.year:
    print('10000')
elif return_date.month > expected_date.month:
    print(f'{500 * (return_date.month - expected_date.month)}')
else:
    print(f'{15 * (return_date.day - expected_date.day)}')
