command = input()
while command != 'End':
    destination = command
    needed_money = float(input())
    collected_money = 0
    while collected_money < needed_money:
        sum_amount = float(input())
        collected_money += sum_amount
    print(f'Going to {destination}!')
    command = input()