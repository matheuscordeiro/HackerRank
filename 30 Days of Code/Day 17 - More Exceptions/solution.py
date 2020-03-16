#!/usr/local/bin/python3

"""Task 

Write a Calculator class with a single method: int power(int,int). The power method takes two integers, n and p, as parameters and returns the integer result of nˆp. 
If either n or p is negative, then the method must throw an exception with the message: n and p should be non-negative.

Note: Do not use an access modifier (e.g.: public) in the declaration for your Calculator class.
"""

import math

#Write your code here
class Calculator:

	def power(self, n, p):
		if n < 0 or p < 0:
			raise ValueError('n and p should be non-negative')
		else:
			return int(math.pow(n, p))

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   