#!/usr/local/bin/python3

"""Task 

Consider a database table, Emails, which has the attributes First Name and Email ID. 
Given N rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com. 
"""

import re

if __name__ == '__main__':
    regex = re.compile('.+@gmail.com$')
    arr = []
    N = int(input())
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if regex.match(emailID):
        	arr.append(firstName)

    arr = sorted(arr)
    for value in arr:
    	print(value)

