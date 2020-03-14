#!/usr/local/bin/python3

"""Task 

In this challenge, you will be given a list of letter heights in the alphabet and a string. 
Using the letter heights given, determine the area of the rectangle highlight in mmˆ2 assuming all letters are 1mm wide.

For example, the highlighted word = torn. Assume the heights of the letters are t=2, o=1, r=1 and n=1. The tallest letter is 2 high and there are 4 letters. 
The hightlighted area will be 2*4 = 8mm^2 so the answer is 8.

Function Description
Complete the designerPdfViewer function in the editor below. It should return an integer representing the size of the highlighted area.
designerPdfViewer has the following parameter(s):
	h: an array of integers representing the heights of each letter
	word: a string
"""

import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
	alphabetic = {}
	for index, letter in enumerate(string.ascii_lowercase):
		alphabetic[letter] = h[index]
	
	tallest = 0
	for letter in word:
		if alphabetic[letter] > tallest:
			tallest = alphabetic[letter]

	return len(word) * tallest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    fptr.write(str(result) + '\n')
    fptr.close()
