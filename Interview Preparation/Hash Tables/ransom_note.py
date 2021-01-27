#!/usr/local/bin/python3

# Ransom Note


def checkMagazine(magazine, note):
	words = {}
	for word in magazine:
		words[word] = words.get(word, 0) + 1

	for word in note:
		if not words.get(word):
			print("No")
			return
		else:
			words[word] -= 1

	print("Yes")
