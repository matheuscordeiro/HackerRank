#!/usr/local/bin/python3

"""Task 

Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
You will then be given an unknown number of names to query your phone book for. 
For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
if an entry for  is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""

n = int(input().strip())
book = {}
search = []
for _ in range(n):
    name, phone = input().strip().split()
    book[name] = phone

while True:
    try:
        name = input().strip()
        search.append(name)
    except EOFError:
        break

for name in search:
    if book.get(name):
        print(f'{name}={book.get(name)}') 
    else:
         print('Not found')