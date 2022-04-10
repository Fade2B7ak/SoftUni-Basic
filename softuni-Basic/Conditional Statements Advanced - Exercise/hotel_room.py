mount = input()
nights = int(input())

studio_cost = 0
apartment_cost = 0

if mount == 'May' or mount == 'October':
    studio_price = 50 #per night
    apartment_price = 65 #per night
    studio_cost = nights * studio_price
    apartment_cost = nights * apartment_price
    if 7 < nights <= 14:
        studio_cost = studio_cost - (studio_cost * 0.05) #discount for > 7 nights may/october
    elif nights > 14:
        studio_cost = studio_cost - (studio_cost * 0.3)
        apartment_cost = apartment_cost - (apartment_cost * 0.1) #discount for => 14 nights
elif mount == 'June' or mount == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    studio_cost = nights * studio_price
    apartment_cost = nights * apartment_price
    if nights > 14:
        studio_cost = studio_cost - (studio_cost * 0.2) #discount for => 14 nights june/september
        apartment_cost = apartment_cost - (apartment_cost * 0.1)
elif mount == 'July' or mount == 'August':
    studio_price = 76
    apartment_price = 77
    studio_cost = nights * studio_price
    apartment_cost = nights * apartment_price
    if nights > 14:
        apartment_cost = apartment_cost - (apartment_cost * 0.1)
print(f"Apartment: {apartment_cost:.2f} lv.")
print(f"Studio: {studio_cost:.2f} lv.")
