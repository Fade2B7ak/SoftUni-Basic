weight = int(input())
length = int(input())

cake_peaces = weight * length

while True:
    peace = input()
    if peace == 'STOP':
        print(f'{cake_peaces} pieces are left.')
        break

    cake_peaces -= int(peace)

    if cake_peaces <= 0:
        print(f'No more cake left! You need {abs(cake_peaces)} pieces more.')
        break