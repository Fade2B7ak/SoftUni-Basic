money_earned = float(input())
year_of_death = int(input())

current_age = 18
even_year_spendings = 12000

for age in range(1800, year_of_death + 1):
    if age % 2 == 0:
        money_earned -= even_year_spendings
        age += 1
        current_age += 1

    elif age % 2 == 1:
        odd_year_spendings = 12000+(50 * current_age)
        money_earned -= odd_year_spendings
        age += 1
        current_age += 1

if money_earned >= 0:
    print(f'Yes! He will live a carefree life and will have {money_earned:.2f} dollars left.')
elif money_earned <= 0:
    print(f'He will need {abs(money_earned):.2f} dollars to survive.')