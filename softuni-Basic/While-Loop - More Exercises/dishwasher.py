bottles_of_detergent = int(input())

detergent_amount = bottles_of_detergent * 750
detergent_needed = 0
number_of_plates = 0
number_of_pots = 0
counter_dishwasher_loading = 0
command = input()

while command != 'End':
    count_of_dishes_for_cleaning = int(command)
    counter_dishwasher_loading += 1
    if counter_dishwasher_loading % 3 == 0:
        detergent_needed = count_of_dishes_for_cleaning * 15
        number_of_pots += count_of_dishes_for_cleaning
    else:
        detergent_needed = count_of_dishes_for_cleaning * 5
        number_of_plates += count_of_dishes_for_cleaning
    detergent_amount -= detergent_needed
    if detergent_amount < 0:
        difference = 0 - detergent_amount
        print(f'Not enough detergent, {difference} ml. more necessary!')
        break
    command = input()

if command == 'End':
    print('Detergent was enough!')
    print(f'{number_of_plates} dishes and {number_of_pots} pots were washed.')
    print(f'Leftover detergent {detergent_amount} ml.')