import math

average_speed = float(input())
litters_per_kms = float(input())


total_distance = 0
needed_hours = 0
total_hours = 0
fuel = 0
distance = 384400
time_on_moon = 3

total_distance = distance * 2
needed_hours = total_distance / average_speed
total_hours = math.ceil(needed_hours) + time_on_moon
fuel = (litters_per_kms * total_distance) / 100

print(math.ceil(total_hours))
print(f'{fuel:.0f}')