mounth = input()
hours = int(input())
people = int(input())
type_of_day = input()

total = 0
total2 = 0

if mounth == 'march' or mounth == 'april' or mounth == 'may':
    if type_of_day == 'day':
        total = hours * 10.5
    elif type_of_day == 'night':
        total = hours * 8.4

elif mounth == 'june' or mounth == 'july' or mounth == 'august':
    if type_of_day == 'day':
        total = hours * 12.6
    elif type_of_day == 'night':
        total = hours * 10.20

if people >= 4:
    total *= 0.9

if hours >= 5:
    total *= 0.5

total2 = total * people

print(f'Price per person for one hour: {total / hours:.2f}')
print(f'Total cost of the visit: {total2:.2f}')