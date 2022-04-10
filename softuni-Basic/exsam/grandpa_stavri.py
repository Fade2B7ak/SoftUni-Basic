days_of_boiling = int(input())

allLiter = 0
average_degrees = 0
total_degrees = 0

for i in range(1, days_of_boiling + 1):
    days_of_boiling = float(input())
    degrees_per_day = float(input())

    allLiter += days_of_boiling
    total_degrees += allLiter * degrees_per_day

    average_degrees = total_degrees / allLiter

if total_degrees <= 38:
    print(f'Liter: {allLiter:.2f}')
    print(f'Degrees: {average_degrees:.2f}')
    print('Not good, you should baking!')
elif 38 < total_degrees <= 42:
    print('Super')
elif 42 < average_degrees:
    print('Dilution with distilled water!')
