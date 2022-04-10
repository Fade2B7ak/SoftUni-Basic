group_budget = float(input())
category = input()
group_of_people = int(input())

money_need = 0
budget = 0
ticket_price = 0

if category == 'Normal':
    ticket_price = 249.99
elif category == 'VIP':
    ticket_price = 499.99

if 1 <= group_of_people <= 4:
    budget = group_budget - ((group_budget / 100) * 75)
elif 5 <= group_of_people <= 9:
    budget = group_budget - ((group_budget / 100) * 60)
elif 10 <= group_of_people <= 24:
    budget = group_budget - ((group_budget / 100) * 50)
elif 25 <= group_of_people <= 49:
    budget = group_budget - ((group_budget / 100) * 40)
else:
    budget = group_budget - ((group_budget / 100) * 25)

money_need = ticket_price * group_of_people
more_money = money_need - budget
money_left = budget - money_need

if money_need > budget:
    print(f'Not enough money! You need {more_money:.2f} leva.')
elif money_need < budget:
    print(f'Yes! You have {money_left:.2f} leva left.')