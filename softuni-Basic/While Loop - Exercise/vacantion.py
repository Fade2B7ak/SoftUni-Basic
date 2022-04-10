needed_money = float(input())
owned_money = float(input())

spend_counter = 0
days = 0

while True:
    action = input()
    amount = float(input())
    days += 1
    if action == 'spend':
        spend_counter += 1
        owned_money -= amount
        if owned_money < 0:
            owned_money = 0

        if spend_counter == 5:
            print("You can't save the money.")
            print(f'{days}')
            break

    else:
        owned_money += amount
        spend_counter = 0

    if owned_money >= needed_money:
        print(f'You saved the money for {days} days.')
        break