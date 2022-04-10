import math
rest_days = int(input())
tom_norm = 30000
# # 30 000 > 24 274 => остават 5725 мин = 95 часа и 25 мин
play_minutes_in_rest_days = rest_days * 127
work_days = 365 - rest_days
play_minutes_in_work_days = work_days * 63
sum_minutes_played = play_minutes_in_rest_days + play_minutes_in_work_days

difference = math.fabs(tom_norm - sum_minutes_played)
hours = difference // 60
minutes = difference % 60

if sum_minutes_played > 30000:
    print("Tom will run away")
    print(f"{hours:.0f} hours and {minutes:.0f} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours:.0f} hours and {minutes:.0f} minutes less for play")

