from sys import maxsize

n = int(input())
odd_sum = 0
odd_min = maxsize
odd_max = -maxsize
even_sum = 0
even_min = maxsize
even_max = -maxsize

for i in range(0, n):
    current_number= float(input())
    if i % 2 == 1:
        even_sum += current_number
        if current_number < even_min:
            even_min = current_number
        if current_number > even_max:
            even_max = current_number
    else:
        odd_sum += current_number
        if current_number < odd_min:
            odd_min = current_number
        if current_number > odd_max:
            odd_max = current_number

if n > 0:
    print(f'OddSum={odd_sum:.2f},')

    if odd_min == maxsize:
        print(f'OddMin=No,')
    else:
        print(f'OddMin={odd_min:.2f},')
    if odd_max == -maxsize:
        print(f'OddMax=No,')
    else:
        print(f'OddMax={odd_max:.2f},')

    print(f'EvenSum={even_sum:.2f},')

    if even_min == maxsize:
        print(f'EvenMin=No,')
    else:
        print(f'EvenMin={even_min:.2f},')

    if even_max == -maxsize:
        print(f'EvenMax=No')
    else:
        print(f'EvenMax={even_max:.2f}')
elif n==0:
    print(f"""OddSum=0.00,
OddMin=No,
OddMax=No,
EvenSum=0.00,
EvenMin=No,
EvenMax=No""")
else:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_min},')
    print(f'OddMax={odd_max},')
    print(f'EvenSum={even_sum:},')
    print(f'EvenMin={even_min:},')
    print(f'EvenMax={even_max}')