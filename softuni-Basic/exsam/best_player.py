command = input()
hattrick = False
best_player = ""
current_max_goals = 0
while command != "END":
    player_name = command
    goals_made = int(input())
    if goals_made > current_max_goals:
        current_max_goals = goals_made
        best_player = player_name
        if goals_made >= 3:
            hattrick = True
            if goals_made >= 10:
                break

    command = input()
if hattrick:
    print(f"{best_player} is the best player!")
    print(f"He has scored {current_max_goals} goals and made a hat-trick !!!")
else:
    print(f"{best_player} is the best player!")
    print(f"He has scored {current_max_goals} goals.")