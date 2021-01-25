#!/usr/local/bin/python3

# 2D Array - DS

def hourglassSum(arr):
	maximum = -64 # 63 is the highest hourglass sum
	for i in range(1,5):
		for j in range(1,5):
			top = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
			center = arr[i][j]
			bottom = arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
			total = top + center + bottom
			if total > maximum:
				maximum = total

	return maximum


arr = [
	[1, 1, 1, 0, 0, 0],
	[0, 1, 0, 0, 0, 0],
	[1, 1, 1, 0, 0, 0],
	[0, 9, 2, -4, -4, 0],
	[0, 0, 0, -2, 0, 0],
	[0, 0, -1, -2, -4, 0]
]
hourglassSum(arr)
