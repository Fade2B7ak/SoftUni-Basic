import math

tournament_count = int(input())
initial_point = int(input())

winner = 2000
finalist = 1200
semi_finalist = 720
points = 0
tournaments_won = 0

for tournament in range(tournament_count):
    stage = input()

    if stage == 'W':
        points += winner
        tournaments_won += 1

    elif stage == 'F':
        points += finalist

    elif stage == 'SF':
        points += semi_finalist

average_poins = math.floor(points / tournament_count)
win_percent = (tournaments_won / tournament_count) * 100
final_points = initial_point + points
print(f'Final points: {final_points}')
print(f'Average points: {average_poins}')
print(f'{win_percent:.2f}%')