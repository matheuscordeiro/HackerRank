#!/usr/local/bin/python3

"""Task 

Given a base-10 integer, n, convert it to binary (base-2). 
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
"""

if __name__ == '__main__':
    n = int(input())
    binary = format(n, 'b')
    count_one = 0
    max_one = 0
    for bit in binary:
        if bit == '1':
            count_one += 1
        else:
            count_one = 0
        if count_one > max_one:
            max_one = count_one

    print(max_one)