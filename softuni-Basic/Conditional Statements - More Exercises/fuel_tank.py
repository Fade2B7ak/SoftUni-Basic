fuel_type = input().lower()
litters_of_fuel_in_the_tank = int(input())

kilometers = 0

good_to_go = fuel_type * litters_of_fuel_in_the_tank
need_to_feel = fuel_type * litters_of_fuel_in_the_tank

if fuel_type != 'diesel' and fuel_type != 'gasoline' and fuel_type != 'gas':
    print('Invalid fuel!')
elif litters_of_fuel_in_the_tank >= 25:
    print(f'You have enough {fuel_type}.')
elif litters_of_fuel_in_the_tank < 25:
    print(f'Fill your tank with {fuel_type}!')
