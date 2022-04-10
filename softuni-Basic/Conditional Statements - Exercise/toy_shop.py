tour_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trucks_price = 2

total_price = puzzles * puzzles_price + dolls * dolls_price + bears * bears_price + minions \
              * minions_price + trucks * trucks_price
toys_count = puzzles + dolls + bears + minions + trucks
discount = 0.25

if toys_count >= 50:
    total_price -= total_price * 0.25

rent = total_price * 0.10

profit = total_price - rent
left_money = abs(profit - tour_price)
needed_money = abs(tour_price - profit)
if profit >= tour_price:
    print(f'Yes! {left_money:.2f} lv left.')
else:
    print(f'Not enough money! {needed_money:.2f} lv needed.')