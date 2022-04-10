first_num = int(input())
second_num = int(input())
operator = input()

result = 0
if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = first_num + second_num
    elif operator == '-':
        result = first_num - second_num
    elif operator == '*':
        result = first_num * second_num
    if result % 2 == 0:
        print(f"{first_num} {operator} {second_num} = {result} - even")
    else:
        print(f"{first_num} {operator} {second_num} = {result} - odd")
elif operator == '/' or operator == '%':
    if second_num == 0:
        print(f"Cannot divide {first_num} by zero")
    elif operator == '/':
        result = first_num / second_num
        print(f"{first_num} / {second_num} = {result:.2f}")
    elif operator == '%':
        result = first_num % second_num
        print(f"{first_num} % {second_num} = {result}")
