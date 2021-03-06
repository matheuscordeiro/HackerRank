#!/usr/local/bin/python3

"""Task 

Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
 - If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
 - If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 Hackos x (the number of days late).
 - If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 Hackos x (the number of days late).
 - If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.
"""

import datetime
return_date=list(map(int, input().rstrip().split()))
expected_date=list(map(int, input().rstrip().split()))
return_date=datetime.date(day=return_date[0], month=return_date[1], year=return_date[2])
expected_date=datetime.date(day=expected_date[0], month=expected_date[1], year=expected_date[2])

if return_date <= expected_date:
    print('0')
elif return_date.year > expected_date.year:
    print('10000')
elif return_date.month > expected_date.month:
    print(f'{500 * (return_date.month - expected_date.month)}')
else:
    print(f'{15 * (return_date.day - expected_date.day)}')
