#!/usr/local/bin/python3

# Minimum Swaps 2

def minimumSwaps(arr):
	arr_sort = sorted(arr)  # O(N*log(N))
	positions = dict([value, key] for key, value in enumerate(arr))
	swaps = 0
	for key, value in enumerate(arr_sort):  # O(N)
		if value != arr[key]:
			temp = arr[key]
			arr[key] = value
			arr[positions[value]] = temp
			
			old_value = positions[value]
			old_index = arr[old_value]
			positions[value] = key
			positions[old_index] = old_value
			swaps += 1

	return swaps


print(minimumSwaps([3,2,1]))
