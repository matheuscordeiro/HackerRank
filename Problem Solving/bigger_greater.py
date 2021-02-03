#!/usr/local/bin/python3


# Bigger is Greater
# Difficulty: Medium


def biggerIsGreater(w):
	size_w = len(w)
	final = None
	position = None
	for i in range(size_w-1, 0, -1):
		j = i - 1
		for k in range(j, -1, -1):
			if w[i] > w[k]:
				if not position or position < k:
					position = k
					value = list(w)
					value[k] = w[i]
					value[i] = w[k]
					tmp = value[:k+1] + sorted(value[k+1:])
					if not final:
						final = tmp
					elif tmp < final:
						final = tmp
				break

	return "".join(final) if final else "no answer"
