import math

loze_plosht = int(input())
grape_per_square = float(input())
wine_couunted_for_sale = int(input())
workers = int(input())


grape_for_wine = loze_plosht * grape_per_square
wine = grape_for_wine * 0.40 / 2.5
wine_left = wine - wine_couunted_for_sale

if wine < wine_couunted_for_sale:
    more_wine_needed = wine_couunted_for_sale - wine
    print(f'It will be a tough winter! More {math.floor(more_wine_needed)} liters wine needed.')
else:
    wine_per_worker = wine_left / workers
    print(f'Good harvest this year! Total wine: {math.floor(wine)} liters.')
    print(f'{math.ceil(wine_left)} liters left -> {math.ceil(wine_per_worker)} liters per person.')