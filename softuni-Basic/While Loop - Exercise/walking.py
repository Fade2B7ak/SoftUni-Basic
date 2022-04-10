goal = 10000
steps_count = 0

while True:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        steps_count += steps
        if steps_count >= goal:
            print("Goal reached! Good job!")
            print(f'{steps_count - goal} steps over the goal!')
        else:
            print(f'{goal - steps_count} more steps to reach goal.')
        break
    steps_count += int(steps)

    if steps_count >= goal:
        print("Goal reached! Good job!")
        print(f'{steps_count - goal} steps over the goal!')
        break