#!/usr/local/bin/python3

"""Task 

Complete the code in the editor below. The variables i, d, and s are already declared and initialized for you. You must:
	1. Declare 3 variables: one of type int, one of type double, and one of type String.
	2. Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your 3 variables.
	3. Use the + operator to perform the following operations: 
		- Print the sum of i plus your int variable on a new line.
		- Print the sum of d plus your double variable to a scale of one decimal place on a new line.
		- Concatenate s with the string you read as input and print the result on a new line.

Note: If you are using a language that doesn't support using + for string concatenation (e.g.: C), 
you can just print one variable immediately following the other on the same line. 
The string provided in your editor must be printed first, immediately followed by the string you read as input.
"""

# Declare second integer, double, and String variables.
first = 0
second = 0.0
third = ''
# Read and save an integer, double, and String to your variables.
first = input()
second = input()
third = input()
# Print the sum of both integer variables on a new line.
print(int(first) + i)

# Print the sum of the double variables on a new line.
print(float(second) + d)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print('{}{}'.format(s, third))
