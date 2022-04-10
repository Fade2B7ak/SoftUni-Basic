import sys

count_of_numbers = int(input())
max_number = sys.maxsize
min_number = -sys.maxsize
for numbers in range(count_of_numbers):
    number = int(input())
    if max_number > number:
        max_number = number
    if min_number < number:
        min_number = number
print(f"Max number: {min_number}")
print(f"Min number: {max_number}")