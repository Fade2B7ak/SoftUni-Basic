budget = float(input())
video_cards_quantity = int(input())
cpu_quantity = int(input())
rams_quantity = int(input())

video_cards_price = video_cards_quantity * 250
cpu_price = video_cards_price * 0.35
ram_price = video_cards_price * 0.10
rams = ram_price * rams_quantity
total = video_cards_price + cpu_price + rams

if video_cards_quantity > cpu_quantity:
    total = total - (total * 0.15)

if budget > total:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")
