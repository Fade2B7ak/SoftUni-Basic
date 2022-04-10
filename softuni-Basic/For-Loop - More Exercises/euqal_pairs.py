import sys

count_of_pairs = int(input())

value = 0
difference = -sys.maxsize
is_difference = False

for number in range(count_of_pairs):
    number_one = int(input())
    number_two = int(input())

    sum_of_numbers = number_one + number_two
    if number == 0:
        value = sum_of_numbers
    else:
        if value != sum_of_numbers:
            difference = abs(sum_of_numbers - value)
            is_difference = True
            value = sum_of_numbers

if is_difference:
    print(f'No, maxdiff={difference}')
else:
    print(f'Yes, value={value}')