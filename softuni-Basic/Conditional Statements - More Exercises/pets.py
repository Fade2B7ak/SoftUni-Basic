import math

days = int(input())
left_food_in_kilos = int(input())
food_per_day_for_dog = float(input())
food_per_day_for_cat = float(input())
food_per_day_for_turtle = float(input())

food_per_day_for_dog *= days #Количеството храна на кучето, за всички дни.
food_per_day_for_cat *= days #Количеството храна на котката, за всички дни.
food_per_day_for_turtle *= days / 1000 #Количеството храна на костенурката, за всички дни.
all_the_food = food_per_day_for_turtle + food_per_day_for_cat + food_per_day_for_dog
all_the_food_left = left_food_in_kilos - all_the_food
more_food_needed = left_food_in_kilos - all_the_food

if all_the_food_left >= 0:
    print(f'{math.floor(all_the_food_left)} kilos of food left.')
else:
    print(f'{math.ceil(abs(more_food_needed))} more kilos of food are needed.')