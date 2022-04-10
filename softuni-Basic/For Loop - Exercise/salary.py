tabs_open = int(input())
salary = int(input())

facebook = 150
instagram = 100
reddit = 50

for tab in range(tabs_open):
    website = input()

    if website == 'Facebook':
        salary -= facebook
    elif website == 'Instagram':
        salary -= instagram
    elif website == 'Reddit':
        salary -= reddit

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)