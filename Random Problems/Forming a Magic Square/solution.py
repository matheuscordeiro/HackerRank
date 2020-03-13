#!/usr/local/bin/python3


"""Task 

We define a magic square to be an n x n matrix of distinct positive integers from 1 to nˆ2 
where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.
You will be given a 3 x 3 matrix s of integers in the inclusive range [1,9]. We can convert any digit a to any other digit b in the range [1,9] at cost of |a-b|. 
Given s, convert it into a magic square at minimal cost. Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range [1,9].
"""

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):

	S1 = [ [4,9,2], [3,5,7], [8,1,6] ]
	S2 = [ [8,1,6], [3,5,7], [4,9,2] ]
	S3 = [ [2,9,4], [7,5,3], [6,1,8] ]
	S4 = [ [6,1,8], [7,5,3], [2,9,4] ]
	S5 = [ [6,7,2], [1,5,9], [8,3,4] ]
	S6 = [ [2,7,6], [9,5,1], [4,3,8] ]
	S7 = [ [8,3,4], [1,5,9], [6,7,2] ]
	S8 = [ [4,3,8], [9,5,1], [2,7,6] ]

	
	squares = [S1, S2, S3, S4, S5, S6, S7, S8]
	
	cost_minimum = 10000
	for square in squares:
		cost_square = 0
		for i in range(0, 3):
			for j in range(0, 3):
				cost_square += abs(square[i][j] - s[i][j])

		if cost_square < cost_minimum:
			cost_minimum = cost_square

	return cost_minimum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')
    fptr.close()    

