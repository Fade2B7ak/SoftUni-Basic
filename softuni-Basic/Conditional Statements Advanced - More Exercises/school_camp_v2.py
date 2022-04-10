season = input()
type_of_group = input()
count_of_students = int(input())
count_of_nights = int(input())


price_for_night = 0
total_cost = 0
type_of_sport = ''

if season == 'Spring':
    if type_of_group == 'girls':
        nights_cost = count_of_students * count_of_nights * 7.20
        type_of_sport = 'Athletics'
        if count_of_students < 10:
            nights_cost = count_of_students * count_of_nights
        elif 10 <= count_of_students < 20:
            total_cost = nights_cost - (nights_cost * 0.05)
        elif 20 <= count_of_students < 50:
            total_cost = nights_cost - (nights_cost * 0.15)
        else:
            total_cost = nights_cost - (nights_cost * 0.5)
elif season == 'Winter':
    if type_of_group == 'girls':
        nights_cost = count_of_students * count_of_nights * 9.60
        type_of_sport = 'Gymnastics'
        if count_of_students < 10:
            nights_cost = count_of_students * count_of_nights
        elif 10 <= count_of_students < 20:
            total_cost = nights_cost - (nights_cost * 0.05)
        elif 20 <= count_of_students < 50:
            total_cost = nights_cost - (nights_cost * 0.15)
        else:
            total_cost = nights_cost - (nights_cost * 0.5)
elif season == 'Summer':
    if type_of_group == 'girls':
        nights_cost = count_of_students * count_of_nights * 15
        type_of_sport = 'Volleyball'
        if count_of_students < 10:
            nights_cost = count_of_students * count_of_nights
        elif 10 <= count_of_students < 20:
            total_cost = nights_cost - (nights_cost * 0.05)
        elif 20 <= count_of_students < 50:
            total_cost = nights_cost - (nights_cost * 0.15)
        else:
            total_cost = nights_cost - (nights_cost * 0.5)

if season == 'Spring':
    if type_of_group == 'boys':
        nights_cost = count_of_students * count_of_nights * 7.20
        type_of_sport = 'Tennis'
        if count_of_students < 10:
            nights_cost = count_of_students * count_of_nights
        elif 10 <= count_of_students < 20:
            total_cost = nights_cost - (nights_cost * 0.05)
        elif 20 <= count_of_students < 50:
            total_cost = nights_cost - (nights_cost * 0.15)
        else:
            total_cost = nights_cost - (nights_cost * 0.5)
elif season == 'Winter':
    if type_of_group == 'boys':
        nights_cost = count_of_students * count_of_nights * 9.60
        type_of_sport = 'Judo'
        if count_of_students < 10:
            nights_cost = count_of_students * count_of_nights
        elif 10 <= count_of_students < 20:
            total_cost = nights_cost - (nights_cost * 0.05)
        elif 20 <= count_of_students < 50:
            total_cost = nights_cost - (nights_cost * 0.15)
        else:
            total_cost = nights_cost - (nights_cost * 0.5)
elif season == 'Summer':
    if type_of_group == 'boys':
        nights_cost = count_of_students * count_of_nights * 15
        type_of_sport = 'Football'
        if count_of_students < 10:
            nights_cost = count_of_students * count_of_nights
        elif 10 <= count_of_students < 20:
            total_cost = nights_cost - (nights_cost * 0.05)
        elif 20 <= count_of_students < 50:
            total_cost = nights_cost - (nights_cost * 0.15)
        else:
            total_cost = nights_cost - (nights_cost * 0.5)
if season == 'Spring':
    if type_of_group == 'mixed':
        nights_cost = count_of_students * count_of_nights * 9.50
        type_of_sport = 'Cycling'
        if count_of_students < 10:
            nights_cost = count_of_students * count_of_nights
        elif 10 <= count_of_students < 20:
            total_cost = nights_cost - (nights_cost * 0.05)
        elif 20 <= count_of_students < 50:
            total_cost = nights_cost - (nights_cost * 0.15)
        else:
            total_cost = nights_cost - (nights_cost * 0.5)
if season == 'Winter':
    if type_of_group == 'mixed':
        nights_cost = count_of_students * count_of_nights * 10
        total_cost = nights_cost
        type_of_sport = 'Ski'
        if count_of_students < 10:
            nights_cost = count_of_students * count_of_nights
        elif 10 <= count_of_students < 20:
            total_cost = nights_cost - (nights_cost * 0.05)
        elif 20 <= count_of_students < 50:
            total_cost = nights_cost - (nights_cost * 0.15)
        else:
            total_cost = nights_cost - (nights_cost * 0.5)

if season == 'Summer':
    if type_of_group == 'mixed':
        nights_cost = count_of_students * count_of_nights * 20
        type_of_sport = 'Swimming'
        if count_of_students < 10:
            nights_cost = count_of_students * count_of_nights
        elif 10 <= count_of_students < 20:
            total_cost = nights_cost - (nights_cost * 0.05)
        elif 20 <= count_of_students < 50:
            total_cost = nights_cost - (nights_cost * 0.15)
        else:
            total_cost = nights_cost - (nights_cost * 0.5)
print(f'{type_of_sport} {total_cost:.2f} lv.')