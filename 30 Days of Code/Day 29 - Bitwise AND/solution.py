#!/usr/local/bin/python3

"""Task 

Consider a database table, Emails, which has the attributes First Name and Email ID. 
Given N rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com. 
"""

def max_bitwise(n, k):
    maximum = 0
    for i in range(1, n+1):
        for j in range(i + 1, n+1):
            bitwise = i & j
            if bitwise > maximum and bitwise < k:
                maximum = bitwise
                if k - maximum == 1:
                    return maximum
    
    return maximum

if __name__ == '__main__':
    t = int(input())
    maximums = []
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])        
        print(max_bitwise(n, k))


