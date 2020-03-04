#!/usr/local/bin/python3

"""Task 

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
For example, arr = [1, 3, 5, 7, 9]. Our minimum sum is 1 + 3 + 5 + 7 = 16 and our maximum sum is 3 + 5 + 7 + 9. We would print
16 24
"""

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
	arr.sort()
	maximum = arr[1] + arr[2] + arr[3] + arr[4]
	minimum = arr[0] + arr[1] + arr[2] + arr[3]
	print(f'{minimum} {maximum}')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
