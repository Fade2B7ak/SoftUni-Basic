budget = float(input())
season = input()

car_class = ''
type_of_car = ''
car_price = 0

if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        car_price = budget * 35 / 100
    elif season == 'Winter':
        type_of_car = 'Jeep'
        car_price = budget * 65 / 100
elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        car_price = budget * 45 / 100
    elif season == 'Winter':
        type_of_car = 'Jeep'
        car_price = budget * 80 / 100
else:
    car_class = 'Luxury class'
    if season == 'Summer' or season == 'Winter':
        type_of_car = 'Jeep'
        car_price = budget * 90 / 100

print(f"{car_class}")
print(f'{type_of_car} - {car_price:.2f}')
