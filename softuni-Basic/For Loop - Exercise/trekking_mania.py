groups_of_climbers = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

# ⦁	Група до 5 човека – изкачват Мусала
# ⦁	Група от 6 до 12 човека – изкачват Монблан
# ⦁	Група от 13 до 25 човека – изкачват Килиманджаро
# ⦁	Група от 26 до 40 човека –  изкачват К2
# ⦁	Група от 41 или повече човека – изкачват Еверест
for group in range(1, groups_of_climbers +1):
    number_of_climbers = int(input())

    if number_of_climbers <= 5:
        musala += number_of_climbers
    elif 6 <= number_of_climbers <= 12:
        montblanc += number_of_climbers
    elif 13 <= number_of_climbers <= 25:
        kilimanjaro += number_of_climbers
    elif 26 <= number_of_climbers <= 40:
        k2 += number_of_climbers
    else:
        everest += number_of_climbers

total_climbers = musala + montblanc + kilimanjaro + k2 + everest
musala_percentage = musala / total_climbers * 100
montblanc_percentage = montblanc / total_climbers * 100
kilimanjaro_percentage = kilimanjaro / total_climbers * 100
k2_percentage = k2 / total_climbers * 100
everest_percentage = everest / total_climbers * 100

print(f'{musala_percentage:.2f}%')
print(f'{montblanc_percentage:.2f}%')
print(f'{kilimanjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')