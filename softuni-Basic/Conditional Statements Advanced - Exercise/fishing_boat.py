budget = int(input())
season = input()
fishermans = int(input())
boat_rent = 0

if season == 'Spring':
    boat_rent = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_rent = 4200
elif season == 'Winter':
    boat_rent = 2600

if fishermans <= 6:
    boat_rent *= 0.9 #100% = 90% -> 90/100 = 0.9
elif fishermans <= 11:
    boat_rent *= 0.85
elif fishermans >= 12:
    boat_rent *= 0.75

if season != "Autumn" and fishermans % 2 == 0:
    boat_rent *= 0.95

difference = abs(budget - boat_rent)
if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")