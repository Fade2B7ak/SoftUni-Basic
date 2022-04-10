budget = float(input())
season = input()
destination = ''
price = 0
type_accommodation = ''

if season == 'summer':
    type_accommodation = 'Camp'
elif season == 'winter':
    type_accommodation = 'Hotel'

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.3
    elif season == 'winter':
        price = budget * 0.7
elif 100 <= budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.4
    elif season == 'winter':
        price = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    if season == 'summer' or season == 'winter':
        type_accommodation = 'Hotel'
        price = budget * 0.9
print(f"Somewhere in {destination}")
print(f"{type_accommodation} - {price:.2f}")
