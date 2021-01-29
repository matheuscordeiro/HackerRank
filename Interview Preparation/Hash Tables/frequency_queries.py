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
