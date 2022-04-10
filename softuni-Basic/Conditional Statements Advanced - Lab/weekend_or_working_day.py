day_of_the_week = input()
type_of_the_day = ''
if day_of_the_week == 'Monday' or day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday'\
        or day_of_the_week == 'Thursday' or day_of_the_week == 'Friday':
    type_of_the_day = "Working day"
elif day_of_the_week == 'Saturday'or day_of_the_week == 'Sunday':
    type_of_the_day = "Weekend"
else:
    type_of_the_day = "Error"
print(type_of_the_day)