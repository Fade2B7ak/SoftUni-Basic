degrees = int(input())
day_time = input()
outfit = ''
shoes = ''

if 10 <= degrees <= 18:
    if day_time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif day_time == 'Afternoon' or day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < degrees <= 24:
    if day_time == 'Morning' or day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif day_time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif degrees >= 25:
    if day_time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif day_time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")