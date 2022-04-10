days_to_stay = int(input())
room_type = input()
assessment = input()

room_price = 18
apartment_price = 25
president_apartment_price = 35

final_price = 0

if room_type == 'room for one person':
    final_price = room_price * (days_to_stay - 1)
elif room_type == 'apartment':
    final_price = apartment_price * (days_to_stay - 1)

    if days_to_stay < 10:
        final_price -= final_price * 0.3
    elif days_to_stay == 10 or days_to_stay <= 15:
        final_price -= final_price * 0.35
    else:
        final_price -= final_price * 0.5
elif room_type == 'president apartment':
    final_price = president_apartment_price * (days_to_stay - 1)

    if days_to_stay < 10:
        final_price -= final_price * 0.1
    elif days_to_stay == 10 or days_to_stay <= 15:
        final_price -= final_price * 0.15
    else:
        final_price -= final_price * 0.2

if assessment == 'positive':
    final_price += final_price * 0.25
elif assessment == 'negative':
    final_price -= final_price * 0.10

print(f'{final_price:.2f}')