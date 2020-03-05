#!/usr/local/bin/python3

"""Task 

Given a  2D Array, A. We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
"""

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maximum = 0
    for i in range(4):
        for j in range(4):
            first_line = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            second_line = arr[i+1][j+1]
            third_line = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            value = first_line + second_line + third_line
            if (i == 0 and j == 0) or (value > maximum):
                maximum = value

    print(maximum)
