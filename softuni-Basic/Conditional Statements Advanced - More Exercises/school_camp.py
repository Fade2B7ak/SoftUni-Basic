season = input()
type_of_group = input()
count_of_students = int(input())
count_of_nights = int(input())

night_cost = 0
price_for_night = 0
total_cost = 0
type_of_sport = ''

if season == 'Winter':
    if type_of_group == 'girls':
        price_for_night = 9.60
        type_of_sport = 'Gymnastics'
    elif type_of_group == 'boys':
        price_for_night = 9.60
        type_of_sport = 'Judo'
    elif type_of_group == 'mixed':
        price_for_night = 10
        type_of_sport = 'Ski'
elif season == 'Spring':
    if type_of_group == 'grils':
        price_for_night = 7.2
        type_of_sport = 'Athletics'
    elif type_of_group == 'boys':
        price_for_night = 7.2
        type_of_sport = 'Tennis'
    elif type_of_group == 'mixed':
        price_for_night = 9.5
        type_of_sport = 'Cycling'
elif season == 'Summer':
    if type_of_group == 'girls':
        price_for_night = 15
        type_of_sport = 'Volleyball'
    elif type_of_group == 'boys':
        price_for_night = 15
        type_of_sport = 'Football'
    elif type_of_group == 'mixed':
        price_for_night = 20
        type_of_sport = 'Swimming'

night_cost = count_of_students * count_of_nights
if count_of_students >= 50:
    total_cost = night_cost - (night_cost * 0.5)
elif 50 > count_of_students >= 20:
    total_cost = night_cost - (night_cost * 0.15)
elif 20 > count_of_students >= 10:
    total_cost = night_cost - (night_cost * 0.05)
else:
    total_cost = count_of_students * count_of_nights
print(f'{type_of_sport} {total_cost:.2f}')