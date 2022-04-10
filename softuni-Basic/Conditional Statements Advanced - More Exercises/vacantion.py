budget = float(input())
season = input()

location = ''
place_to_stay = ''
price = 0

if budget <= 1000:
    place_to_stay = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif 1000 < budget <= 3000:
    place_to_stay = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.60
else:
    place_to_stay = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.9
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.9

print(f'{location} - {place_to_stay} - {price:.2f}')