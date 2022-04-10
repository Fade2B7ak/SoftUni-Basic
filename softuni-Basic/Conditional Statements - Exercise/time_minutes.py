hours = int(input())
minutes = int(input())

minutes += 15

if minutes >= 60:
    hours += 1
    minutes %= 60

if hours > 23:
    hours = 0
if minutes <= 9:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')