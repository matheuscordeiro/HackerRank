#!/usr/local/bin/python3

import math

# Complete the encryption function below.
def encryption(s):
	s_no_spaces = ''
	size_s = 0
	# Instead the code below, we can use len(s) and s.replace(' ', '')
	for value in s:
		if s:
			s_no_spaces = f'{s_no_spaces}{s}'
			size_s += 1
	
	sqrt = math.sqrt(size_s)
	rows = int(sqrt)
	columns = math.ceil(sqrt)
	if rows * columns < size_s:
		rows = columns

	result = ''
	for j in range(0, columns):
		jump = j
		if result:
			result = f'{result} '
		for i in range(0, rows):
			if jump < size_s:
				result = f'{result}{s_no_spaces[jump]}'
				jump += columns

	return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = encryption(s)
    fptr.write(result + '\n')
    fptr.close()
