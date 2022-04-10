hours = int(input())
day_of_week = input()

if (hours < 10 or hours >= 18) or day_of_week == "Sunday":
    day_of_week = "closed"
else:
    day_of_week = "open"
print(day_of_week)