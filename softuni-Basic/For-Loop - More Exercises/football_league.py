stadion_capacity = int(input())
fens_count = int(input())

sector = ''
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for fens in range(1, fens_count + 1):
    sector = input()
    if sector == 'A':
        sector_a += 1
    elif sector == 'B':
        sector_b += 1
    elif sector == 'V':
        sector_v += 1
    elif sector == 'G':
        sector_g += 1


sector_a = sector_a / fens_count * 100
sector_b = sector_b / fens_count * 100
sector_v = sector_v / fens_count * 100
sector_g = sector_g / fens_count * 100
total_fens = fens_count / stadion_capacity * 100

print(f'{sector_a:.2f}%')
print(f'{sector_b:.2f}%')
print(f'{sector_v:.2f}%')
print(f'{sector_g:.2f}%')
print(f'{abs(total_fens):.2f}%')