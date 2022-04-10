loads_count = int(input())

bus = 0
truck = 0
train = 0
total_load = 0

for load in range(1, loads_count + 1):
    current_mass = int(input())
    total_load += current_mass
    if current_mass <= 3:
        bus += current_mass

    elif current_mass <= 11:
        truck += current_mass

    elif current_mass >= 12:
        train += current_mass

bus_price = bus * 200
truck_price = truck * 175
train_price = train * 120
average_price = (bus_price + truck_price + train_price) / total_load
percentage_bus = bus / total_load * 100
percentage_truck = truck / total_load * 100
percentage_train = train / total_load * 100

print(f'{average_price:.2f}')
print(f'{percentage_bus:.2f}%')
print(f'{percentage_truck:.2f}%')
print(f'{percentage_train:.2f}%')
