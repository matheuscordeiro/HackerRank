#!/usr/local/bin/python3

N = 100

# Complete the countSort function below.
def countSort(arr):
	numbers = {}
	for i in arr:
		numbers[int(i[0])] = numbers.get(int(i[0]), 0) + 1

	for i in range(1, N):
		numbers[i] = numbers.get(i, 0) + numbers.get(i-1, 0)

	size_arr = len(arr)
	arr_sorted = [0] * size_arr
	for i in range(size_arr-1, -1, -1):
		position = int(arr[i][0])
		value = numbers[position]
		if i + 1 <= size_arr/2:
			arr_sorted[value-1] = '-'
		else:
			arr_sorted[value-1] = arr[i][1]

		numbers[position] -= 1

	print(' '.join(arr_sorted))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
