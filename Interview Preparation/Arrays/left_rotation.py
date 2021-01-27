#!/usr/local/bin/python3

# Left Rotation

def rotLeft(a, d):
	size_a = len(a)
	new_a = [0] * size_a
	walk = d % size_a
	for key, value in enumerate(a):  # O(a)
		new_a[key-walk] = value

	return new_a

rotLeft([1, 2, 3, 4, 5,], 4)