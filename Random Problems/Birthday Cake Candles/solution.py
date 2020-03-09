#!/usr/local/bin/python3

"""Task 

You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. 
When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.
For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 4, 4, 1, 3, she will be able to blow out 2 candles successfully, 
since the tallest candles are of height 4 and there are 2 such candles.

Function Description
Complete the function birthdayCakeCandles in the editor below. It must return an integer representing the number of candles she can blow out.

birthdayCakeCandles has the following parameter(s):
    ar: an array of integers representing candle heights

"""

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    maximum = 0
    count_maximum = {}
    for candle in ar:
        if candle > maximum:
            maximum = candle
            count_maximum[maximum] = 1
        elif candle == maximum:
            count_maximum[maximum] += 1

    return count_maximum[maximum]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
    