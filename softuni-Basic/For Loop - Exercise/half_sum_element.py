import sys
n = int(input())

nums_sum = 0
biggest_num = -sys.maxsize

for number in range(n):
    num = int(input())
    nums_sum += num

    if num > biggest_num:
        biggest_num = num

other_nums = nums_sum - biggest_num

if biggest_num == other_nums:
    print('Yes')
    print(f'Sum = {biggest_num}')
else:
    print("No")
    print(f'Diff = {abs(biggest_num - other_nums)}')