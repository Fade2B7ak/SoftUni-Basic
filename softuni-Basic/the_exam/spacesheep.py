import math

width = float(input())
length = float(input())
height = float(input())
average_height = float(input())

volume_of_the_rocket = 0
volume_per_room = 0
space_for_people = 0
space_till_the_roof = 0.40
room_width = 2
room_length = 2

volume_of_the_rocket = width * length * height
volume_per_room = (average_height + space_till_the_roof) * room_length * room_width
space_for_people = volume_of_the_rocket / volume_per_room

if 3 <= space_for_people <= 10:
    print(f'The spacecraft holds {math.floor(space_for_people)} astronauts.')
elif 3 > space_for_people:
    print('The spacecraft is too small.')
else:
    print('The spacecraft is too big.')