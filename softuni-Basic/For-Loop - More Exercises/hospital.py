period_in_days = int(input())

doctors = 7
total_treated_patients = 0
total_untreated_patients = 0

for period in range(1, period_in_days +1):
    patients_per_day = int(input())
    if period % 3 == 0:
        if total_untreated_patients > total_treated_patients:
            doctors += 1
    if patients_per_day <= doctors:
        total_treated_patients += patients_per_day
    else:
        total_treated_patients += doctors
        total_untreated_patients += (patients_per_day - doctors)

print(f'Treated patients: {total_treated_patients}.')
print(f'Untreated patients: {total_untreated_patients}.')