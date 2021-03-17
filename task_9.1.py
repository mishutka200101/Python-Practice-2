f = int(input())
s = int(input())
first_books = []
second_books = []
for i in range(0, f):
    first_books.insert(i, input())
for i in range(0, s):
    second_books.insert(i, input())
for i in range(0, s):
    if second_books[i] in first_books:
        print('YES')
    else:
        print('NO')
