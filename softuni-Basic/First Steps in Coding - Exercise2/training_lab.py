from math import floor

length = float(input())
width = float(input())

place_length = 120
place_width = 70

rows = 1 / place_length
rows = floor(rows)

rows2 = (width - 100) / place_width
rows2 = floor(rows)

seats = (rows * rows2) - 3
print(f'{seats}')