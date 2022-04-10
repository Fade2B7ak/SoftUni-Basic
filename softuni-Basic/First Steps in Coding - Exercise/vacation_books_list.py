pages_count = int(input())
pages_per_hour = int(input())
day_per_book = int(input())

time_for_the_book = pages_count / pages_per_hour
hours_per_day = time_for_the_book / day_per_book
print(round(hours_per_day))
