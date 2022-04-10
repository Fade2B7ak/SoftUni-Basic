start = int(input())
stop = int(input())
magic_number = int(input())

count_of_combinations = 0
combination_is_found = False

for first_number in range(start, stop +1):
    for second_number in range(start, stop +1):
        count_of_combinations += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            break

    if combination_is_found:
     break
if combination_is_found:
    print(f'Combination N:{count_of_combinations} ({first_number} + {second_number} = {magic_number})')
else:
    print(f'{count_of_combinations} combinations - neither equals {magic_number}')