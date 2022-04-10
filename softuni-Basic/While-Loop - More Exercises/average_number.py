numbers = int(input())
number = 0
sum = 0

for number in range(numbers):
    current_number = int(input())
    sum += current_number
    number = sum / numbers

print(f'{number:.2f}')