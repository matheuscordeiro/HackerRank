#!/usr/local/bin/python3

"""Task 

Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and 
odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.
"""

T = int(input())
S = []
for _ in range(T):
    S.append(input())

for entry in S:
    even = ''
    odd = ''
    for index, value in enumerate(entry):
        if index % 2 == 0:
            even += value
        else:
            odd += value

    print(even, end=' ')
    print(odd)
