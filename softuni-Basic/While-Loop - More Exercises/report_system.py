expected_amount = int(input())
command = input()

count_debit = 0
obtained_money = 0
cash_payment = 0
card_payment = 0
cash_purchase = 0
card_purchase = 0

cs = 0
cc = 0

while command != 'End':
    amount = int(command)
    count_debit += 1

    if amount < 0:
        continue

    if count_debit % 2 == 0:
        if amount < 10:
            print('Error in transaction!')
        else:
            print('Product sold!')
            obtained_money += amount
            card_purchase += amount
            card_payment += 1
    else:
        if amount > 100:
            print('Error in transaction!')
        else:
            print('Product sold!')
            obtained_money += amount
            cash_purchase += amount
            cash_payment += 1
    if expected_amount <= obtained_money:
        break

    command = input()

if cash_purchase > 0:
    cs += cash_purchase / cash_payment
if card_purchase > 0:
    cc += card_purchase / card_payment

if obtained_money >= expected_amount:
    print(f'Average CS: {cs:.2f}')
    print(f'Average CC: {cc:.2f}')
if command == 'End':
    print('Failed to collect required money for charity.')
