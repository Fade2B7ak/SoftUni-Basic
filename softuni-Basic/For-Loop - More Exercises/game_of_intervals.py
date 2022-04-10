turns_in_the_game = int(input())

total_sum = 0
invalid_number = 0
first_number = 0
second_number = 0
third_number = 0
fourth_number = 0
fifth_number = 0

for number in range(turns_in_the_game):
    numbers = int(input())
    if 0 <= numbers <= 9:
        first_number += 1
        total_sum += numbers * 0.2
    elif 10 <= numbers <= 19:
        second_number += 1
        total_sum += numbers * 0.3
    elif 20 <= numbers <= 29:
        third_number += 1
        total_sum += numbers * 0.4
    elif 30 <= numbers <= 39:
        fourth_number += 1
        total_sum += 50
    elif 40 <= numbers <= 50:
        fifth_number += 1
        total_sum += 100
    else:
        invalid_number += 1
        total_sum -= total_sum / 2

low_total = (first_number / turns_in_the_game) * 100
mid_total = (second_number / turns_in_the_game) * 100
avg_total = (third_number / turns_in_the_game) * 100
high_total = (fourth_number / turns_in_the_game) * 100
above_total = (fifth_number / turns_in_the_game) * 100
invalid_total = (invalid_number / turns_in_the_game) * 100

print(f'{total_sum:.2f}')
print(f'From 0 to 9: {low_total:.2f}%')
print(f'From 10 to 19: {mid_total:.2f}%')
print(f'From 20 to 29: {avg_total:.2f}%')
print(f'From 30 to 39: {high_total:.2f}%')
print(f'From 40 to 50: {above_total:.2f}%')
print(f'Invalid numbers: {invalid_total:.2f}%')