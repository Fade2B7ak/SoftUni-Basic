days = int(input())
basketball_shoes = 0.40
percent_for_shoes = days * (40 / 100)
price_for_shoes = days - percent_for_shoes

basketball_suit = 0.20
percent_for_suit = price_for_shoes * (20 / 100)
price_for_suit = price_for_shoes - percent_for_suit

basketball_ball = 0.25
percent_for_ball = price_for_suit * (25 / 100)

basketball_accesories = 0.20
percent_for_accesories = percent_for_ball * (20 / 100)
total_cost = (days + price_for_shoes + price_for_suit + percent_for_ball + percent_for_accesories)
print(total_cost)