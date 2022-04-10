nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00

nylon_quantity = int(input())
paint_quantity = int(input())
thinner_quantity = int(input())
working_hours = int(input())

sum_nylon_price = (nylon_quantity + 2) * nylon_price
sum_paint_price = (paint_quantity + (paint_quantity * 10 / 100)) * paint_price
sum_thinner_prince = thinner_quantity * thinner_price

supplies_prince_sum = sum_thinner_prince + sum_paint_price + sum_nylon_price + 0.40
workers_price = (supplies_prince_sum * (30/100)) * 8

total_price_sum = supplies_prince_sum + workers_price

print(total_price_sum)
