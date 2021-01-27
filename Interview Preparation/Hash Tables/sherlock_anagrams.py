#!/usr/local/bin/python3

# Sherlock and Anagrams

def sherlockAndAnagrams(s):
	total = 0
	substrings = {}
	size_s = len(s)
	for i, _ in enumerate(s):
		j = i
		while j < size_s:
			sorted_s = "".join(sorted(s[i:j+1]))
			total += substrings.get(sorted_s, 0)
			substrings[sorted_s] = substrings.get(sorted_s, 0) + 1
			j += 1

	return total


print(sherlockAndAnagrams('ifailuhkqq'))