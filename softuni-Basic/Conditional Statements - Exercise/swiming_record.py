from math import floor

world_record_in_seconds = float(input())
distance_in_metters = float(input())
time_per_metter = float(input())

distance_in_metters_in_seconds = distance_in_metters * time_per_metter
time_delay = floor(distance_in_metters  // 15) * 12.5
time_sum = distance_in_metters_in_seconds + time_delay
needed_seconds = time_sum - world_record_in_seconds
if world_record_in_seconds > time_sum:

    print(f"Yes, he succeeded! The new world record is {time_sum:.2f} seconds.")
else:
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")