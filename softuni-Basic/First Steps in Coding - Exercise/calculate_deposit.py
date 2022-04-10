deposit = float(input())
period_time = int(input())
annual_interest = float(input())

due_interest = deposit * (annual_interest / 100)
monthly_interest = due_interest / 12
result = deposit + period_time * monthly_interest
print(result)
