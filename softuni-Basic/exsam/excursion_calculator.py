count_of_people = int(input())
type_of_season = input()

price_for_night_per_person = 0
discount = 0
price_raise = 0
total_cost = 0

if type_of_season == 'spring':
    if count_of_people <= 5:
        price_for_night_per_person = 50
        total_cost = count_of_people * price_for_night_per_person
    elif count_of_people > 5:
        price_for_night_per_person = 48
        total_cost = count_of_people * price_for_night_per_person
elif type_of_season == 'summer':
    total_cost = count_of_people * price_for_night_per_person
    discount = 0.15
    if count_of_people <= 5:
        price_for_night_per_person = 48.50
        total_cost = count_of_people * price_for_night_per_person
        total_cost -= total_cost * discount
    elif count_of_people > 5:
        price_for_night_per_person = 45
        total_cost = count_of_people * price_for_night_per_person
        total_cost -= total_cost * discount
elif type_of_season == 'autumn':
    if count_of_people <= 5:
        price_for_night_per_person = 60
        total_cost = count_of_people * price_for_night_per_person
    elif count_of_people > 5:
        price_for_night_per_person = 49.50
        total_cost = count_of_people * price_for_night_per_person
elif type_of_season == 'winter':
    total_cost = count_of_people * price_for_night_per_person
    price_raise = 0.08
    if count_of_people <= 5:
        price_for_night_per_person = 86
        total_cost = count_of_people * price_for_night_per_person
        total_cost += total_cost * price_raise
    elif count_of_people > 5:
        price_for_night_per_person = 85
        total_cost = count_of_people * price_for_night_per_person
        total_cost += total_cost * price_raise
print(f'{total_cost:.2f} leva.')