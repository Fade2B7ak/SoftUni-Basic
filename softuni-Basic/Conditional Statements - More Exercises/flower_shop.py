import math

count_of_magnolias = int(input())
count_of_hyacinths = int(input())
count_of_roses = int(input())
count_of_cacti = int(input())
price_for_the_gift = float(input())

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.50
cacti_price = 8

total_price = count_of_cacti * cacti_price + count_of_roses * roses_price + count_of_hyacinths * hyacinths_price \
              + count_of_magnolias * magnolias_price
profit = total_price - (total_price * 0.05)
money_left = math.floor(profit - price_for_the_gift)
money_to_borrow = math.ceil(price_for_the_gift - profit)

if money_left >= 0:
    print(f'She is left with {money_left} leva.')
else:
    print(f'She will have to borrow {money_to_borrow} leva.')