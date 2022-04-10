cats = int(input())

cat_counter = 1
group1 = 0
group2 = 0
group3 = 0
total_food_in_grams = 0

while cat_counter <= cats:
    grams_food = float(input())
    total_food_in_grams += grams_food
    if 100 <= grams_food <= 199:
        group1 += 1
    elif 200 <= grams_food <= 299:
        group2 += 1
    elif 300 <= grams_food <= 400:
        group3 += 1
    cat_counter += 1
total_food_in_grams /= 1000
food_price = total_food_in_grams * 12.45

print(f'Group 1: {group1} cats.')
print(f'Group 2: {group2} cats.')
print(f'Group 3: {group3} cats.')
print(f'Price for food per day: {food_price:.2f} lv.')
