#!/usr/local/bin/python3

# Frequency queries


def freqQuery(queries):
	result = []
	numbers = {}
	occurrences = {}
	for operation, value in queries:
		if operation == 1:
			quantity = numbers.get(value, 0)
			if quantity > 0:
				occurrences[quantity] = occurrences[quantity] - 1

			numbers[value] = numbers.get(value, 0) + 1
			occurrences[numbers[value]] = occurrences.get(numbers[value], 0) + 1

		elif operation == 2:
			quantity = numbers.get(value, 0)
			if quantity > 0:
				numbers[value] = quantity - 1
				occurrences[quantity] = occurrences[quantity] - 1
				occurrences[quantity - 1] = occurrences.get(quantity - 1, 0) + 1
		else:
			result.append(1) if occurrences.get(value) else result.append(0)

	return result


print(freqQuery([(1,89), (3,15), (1, 12), (1, 47), (1, 23), (1, 66), (2, 28), (3, 2), (2, 15), (1, 16), (3,16), (1,17), (1,73), (2,44), (3,14), (2,30), (2,38), (2,4), (1,4), (2,35), (1,28), (1,9), (1,68), (3,1), (3,33), (3,5)]))