#!/usr/local/bin/python3

"""Task 

Given an integer, n, print its first 10 multiples. 
Each multiple n x i (where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.
"""

n = int(input())
for i in range(1, 11):
    print(f'{n} x {i} = {n*i}')
