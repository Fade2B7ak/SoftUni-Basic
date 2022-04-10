book_name = input()

books_count = 0
found_it = False
book = input()

while book != 'No More Books':
    if book == book_name:
        found_it = True
        break
    books_count +=1

    book = input()

if found_it:
    print(f'You checked {books_count} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {books_count} books.')