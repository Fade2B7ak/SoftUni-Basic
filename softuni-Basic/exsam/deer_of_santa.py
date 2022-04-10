import math



count_of_days = int(input()) #Дните които Дядо Коледа отсъства
food_in_kilos_left = int(input())
food_for_first_deer_per_day = float(input())
food_for_second_deer_per_day = float(input())
food_for_third_deer_per_day = float(input())

total_food_for_fist = count_of_days * food_for_first_deer_per_day
total_food_for_second = count_of_days * food_for_second_deer_per_day
total_food_for_third = count_of_days * food_for_third_deer_per_day
total_food_needed = total_food_for_fist + total_food_for_second + total_food_for_third


if total_food_needed <= food_in_kilos_left:
    food_left = food_in_kilos_left - total_food_needed
    print(f'{math.floor(food_left)} kilos of food left.')
elif total_food_needed > food_in_kilos_left:
    more_food = total_food_needed - food_in_kilos_left
    print(f'{math.ceil(more_food)} more kilos of food are needed.')