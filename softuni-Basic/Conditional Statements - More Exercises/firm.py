import math

needed_hours = int(input())
days_for_finish = int(input())
workers_working_overtime = int(input())

working_hours = (days_for_finish - (days_for_finish * 0.1)) * 8
overtime_hours = workers_working_overtime * 2 * days_for_finish
total_working_hours = math.floor(working_hours + overtime_hours)

diff_hours = abs(total_working_hours - needed_hours)

if total_working_hours >= needed_hours:
    print(f"Yes!{diff_hours} hours left.")
else:
    print(f"Not enough time!{diff_hours} hours needed.")