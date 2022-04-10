lenght = int(input())
width = int(input())
hight = int(input())
percent = float(input())

aquarium_volume = lenght * width * hight
volume_in_litters = aquarium_volume / 1000
occupied_volime = percent / 100

litters_needed = volume_in_litters * (1 - occupied_volime)
print(litters_needed)
