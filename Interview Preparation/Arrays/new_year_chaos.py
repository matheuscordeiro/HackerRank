#!/usr/local/bin/python3

# New Year Chaos

def minimumBribes(q):
	indexes = dict((value, key) for key, value in enumerate(q))

	bribe = 0
	size_q = len(q)
	for i in range(size_q, 0, -1):
		position = indexes[i]
		destine_position = i-1
		bribe_person = 0

		while q[destine_position] != i:
			# swap values
			tmp = q[position+1]
			q[position+1] = i
			q[position] = tmp

			# update indexes
			indexes[tmp] = position
			indexes[i] = position + 1

			bribe_person += 1
			position += 1

		if bribe_person > 2:
			print("Too chaotic")
			return

		bribe += bribe_person
	
	print(bribe)

minimumBribes([2, 5, 1, 3, 4])