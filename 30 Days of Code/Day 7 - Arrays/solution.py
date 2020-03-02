#!/usr/local/bin/python3

"""Task 

Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
"""

n = int(input())
arr = list(map(int, input().rstrip().split()))
size = len(arr)
for index in range(size-1, -1, -1):
	print(arr[index], end=' ')
