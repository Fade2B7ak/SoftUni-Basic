roses = 5
dahlias = 3.80
tulips = 2.80
narcissus = 3
gladiolus = 2.50

type_flowers = input()
flowers_count = int(input())
budget = int(input())



if type_flowers == 'Roses':
    price = flowers_count * roses
elif type_flowers == 'Dahlias':
    price = flowers_count * dahlias
elif type_flowers == 'Tulips':
    price = flowers_count * tulips
elif type_flowers == 'Narcissus':
    price = flowers_count * narcissus
elif type_flowers == 'Gladiolus':
    price = flowers_count * gladiolus

if type_flowers == 'Roses' and flowers_count >= 80:
    price = price - (price * 0.10)
elif type_flowers == 'Dahlias' and flowers_count >= 90:
    price = price - (price * 0.15)
elif type_flowers == 'Tulips' and flowers_count >= 80:
    price = price - (price * 0.15)
elif type_flowers == 'Narcissus' and flowers_count <= 120:
    price = price + (price * 0.15)
elif type_flowers == 'Gladiolus' and flowers_count <= 80:
    price = price + (price * 0.2)

if budget >= price:
    money_left = budget - price
    print(f"Hey, you have a great garden with {flowers_count} {type_flowers} and {money_left:.2f}"
          f" leva left.")
else:
    money_needed = price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")