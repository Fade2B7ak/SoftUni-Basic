food_in_kgs = int(input())


total_food = 0
food_ate_per_day = 0

command = input()

while command != 'Adopted':
    food_ate_per_day = int(command)
    total_food += food_ate_per_day
    food_in_grs = food_in_kgs * 1000
    command = input()

food = total_food - food_in_grs

if food <= food_in_grs:
    print(f'Food is enough! Leftovers: {food} grams.')
elif food >= food_in_grs:
    print(f'Food is not enough. You need {food} grams more.')