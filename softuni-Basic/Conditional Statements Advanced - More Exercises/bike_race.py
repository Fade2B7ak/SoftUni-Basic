junior_bikers = int(input())
senior_bikers = int(input())
trace = input()

total_tax_for_entry = 0
costs = 0.05

if trace == 'trail':
    total_tax_for_entry = (junior_bikers * 5.5) + (senior_bikers * 7)
elif trace == 'cross-country':
    total_tax_for_entry = (junior_bikers * 8) + (senior_bikers * 9.50)
    if junior_bikers + senior_bikers >= 50:
        total_tax_for_entry -= total_tax_for_entry * 0.25
elif trace == 'downhill':
    total_tax_for_entry = (junior_bikers * 12.25) + (senior_bikers * 13.75)
elif trace == 'road':
    total_tax_for_entry = (junior_bikers * 20) + (senior_bikers * 21.50)
final_cost = total_tax_for_entry * costs
money_left_for_charity = total_tax_for_entry - final_cost

print(f'{money_left_for_charity:.2f}')