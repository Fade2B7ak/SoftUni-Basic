locations = int(input())

gold_dug = 0
count = 0
average_gold = 0
count_one = False
count_two = False

while locations > 0:
    expected_gold = float(input())
    mining_days = int(input())
    while mining_days > 0:
        gold_dug += float(input())
        mining_days -= 1
        count += 1
    if mining_days == 0:
        average_gold = gold_dug / count
        if average_gold >= expected_gold:
            print(f'Good job! Average gold per day: {average_gold:.2f}')
            gold_dug -= gold_dug
            average_gold = 0
            count = 0
            locations -= 1
        else:
            average_gold = expected_gold - average_gold
            print(f'You need {average_gold:.2f} gold.')
            gold_dug = 0
            average_gold = 0
            count = 0
            locations -= 1
