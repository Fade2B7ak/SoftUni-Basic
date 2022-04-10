import math

chrysanthemums_bought = int(input())
roses_bought = int(input())
tulips_bought = int(input())
current_season = input()
type_of_day = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
total_price = 0
bouquet_price = 0


if current_season == 'Summer' or current_season == 'Spring':
    chrysanthemums_price = 2
    roses_price = 4.10
    tulips_price = 2.50
elif current_season == 'Autumn' or current_season == 'Winter':
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15
total_flowers_bought = chrysanthemums_bought + roses_bought + tulips_bought
bouquet_price = (chrysanthemums_price * chrysanthemums_bought) + (roses_price * roses_bought) + \
                (tulips_price * tulips_bought)

if type_of_day == 'Y':
    bouquet_price = bouquet_price + (bouquet_price * 0.15)
    if tulips_bought > 7 and current_season == 'Spring':
        bouquet_price = bouquet_price - (bouquet_price * 5) / 100
if roses_bought >= 10 and current_season == 'Winter':
    bouquet_price = bouquet_price - (bouquet_price * 10) / 100
if total_flowers_bought > 20:
    bouquet_price = bouquet_price - (bouquet_price * 20) / 100

total_boquet_price = bouquet_price + 2
print(f'{total_boquet_price:.2f}')