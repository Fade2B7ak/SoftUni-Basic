from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1 / 8
break_time = break_duration * 1 / 4
rest_time = break_duration - break_time - lunch_time

if rest_time >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with " f"{ceil(rest_time - episode_duration)} "
          f"minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need " f"{ceil(episode_duration - rest_time)} "
          f"more minutes.")