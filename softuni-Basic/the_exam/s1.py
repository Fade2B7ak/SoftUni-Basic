locations = int(input())

gold_dug = 0
count = 0
average_gold = 0
count_one = False
count_two = False

while locations > 0:  # Докато локацийте са по-големи от 0 ще се върти цикъла
    expected_gold = float(input())  # Това е очаквания среден добив на злато за ден
    mining_days = int(input())  # Дните в които ще се копае в дадена локация
    while mining_days > 0:  # Докато дните за копаене са по-големи от 0 ще се върти цикъла
        gold_dug += float(input())  # Изкопано злато на ден
        mining_days -= 1  # Намаляваме дните с 1
        count += 1  # Този каунтър е за деленето по-късно за да получим средния добив на ден
    if mining_days == 0:
        average_gold = gold_dug / count  # Делим на дните за копаене (КАУНТЪРА) за да получим среден, дневен добив.
        if average_gold >= expected_gold:
            print(f'Good job! Average gold per day: {average_gold:.2f}.')
            gold_dug -= gold_dug  # 1
            average_gold = 0  # 2
            count = 0  # 3
            locations -= 1  # 4
        else:
            average_gold = expected_gold - average_gold
            print(f'You need {average_gold:.2f} gold.')
            gold_dug = 0
            average_gold = 0
            count = 0
            locations -= 1