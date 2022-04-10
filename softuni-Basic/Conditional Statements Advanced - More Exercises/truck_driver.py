season = input()
kilometers = int(input())

taxes = 0
price_per_kilometer = 0
salary = 0
salary_after_taxes = 0

if kilometers <= 5000:
    if season == 'Autumn' or season == 'Spring':
        price_per_kilometer = 0.75
    elif season == 'Summer':
        price_per_kilometer = 0.90
    elif season == 'Winter':
        price_per_kilometer = 1.05
elif 5000 < kilometers <= 10000:
    if season == 'Autumn' or season == 'Spring':
        price_per_kilometer = 0.95
    elif season == 'Summer':
        price_per_kilometer = 1.10
    elif season == 'Winter':
        price_per_kilometer = 1.25
elif 10000 < kilometers <= 20000:
    if season == 'Autumn' or season == 'Spring' or season == 'Summer' or season == 'Winter':
        price_per_kilometer = 1.45

salary = kilometers * price_per_kilometer
total_salary = salary * 4
salary_after_taxes = total_salary - (total_salary * 0.10)

print(f'{salary_after_taxes:.2f}')