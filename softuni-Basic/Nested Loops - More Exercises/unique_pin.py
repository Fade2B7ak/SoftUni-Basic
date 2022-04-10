first_number = int(input())
second_number = int(input())
third_number = int(input())

for num1 in range(2, first_number +1, 2):
    for num2 in range(2, second_number + 1):
        for num3 in range(2, third_number + 1, 2):
            if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                print(f'{num1}{num2}{num3}')