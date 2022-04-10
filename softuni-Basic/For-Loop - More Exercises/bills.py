months = int(input())

electricity_bill = 0
water_bill = 20
internet_bill = 15
others_bills = 0
water = 0
internet = 0

for month in range(1, months + 1):
    electricity = float(input())
    electricity_bill += electricity
    internet += internet_bill
    water += water_bill

others_bills = (electricity_bill + internet + water) * 1.2
average_bills_per_month = (electricity_bill + internet + water + others_bills) / months


print(f'Electricity: {electricity_bill:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {others_bills:.2f} lv')
print(f'Average: {average_bills_per_month:.2f} lv')