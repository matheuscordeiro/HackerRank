#!/usr/local/bin/python3

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