#!/usr/local/bin/python3

"""Task 

Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
 - If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
 - If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 Hackos x (the number of days late).
 - If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 Hackos x (the number of days late).
 - If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.
"""

return_date=list(map(int, input().rstrip().split()))
expected_date=list(map(int, input().rstrip().split()))

if return_date[0] <= expected_date[0] and return_date[1] <= expected_date[1] and return_date[2] <= expected_date[2]:
    print('0')
elif return_date[2] > expected_date[2]:
    print('10000')
elif return_date[1] > expected_date[1]:
    print(f'{500 * (return_date[1] - expected_date[1])}')
else:
    print(f'{15 * (return_date[0] - expected_date[0])}')
