hour_of_exam = int(input())
minute_of_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

state = ''
time = 0

time_of_exam_in_minutes = hour_of_exam * 60 + minute_of_exam 
time_of_arrival_in_minutes = arrival_hour * 60 + arrival_minute

if time_of_arrival_in_minutes > time_of_exam_in_minutes:
    state = 'Late'
    print(state)
    time = time_of_arrival_in_minutes - time_of_exam_in_minutes
    if time >= 60:
        print(f"{(time // 60)}:{time % 60:0>2d} hours after the start")
    elif time < 60:
        print(f"{time} minutes after the start")
elif (time_of_exam_in_minutes - time_of_arrival_in_minutes) <= 30:
    state = 'On time'
    print(state)
    time = time_of_exam_in_minutes - time_of_arrival_in_minutes
    if time != 0:
        if time >= 60:
            print(f"{(time // 60)}:{time % 60:0>2d} hours before the start")
        elif time < 60:
            print(f"{time} minutes before the start")
elif (time_of_exam_in_minutes - time_of_arrival_in_minutes) > 30:
    state = 'Early'
    print(state)
    time = time_of_exam_in_minutes - time_of_arrival_in_minutes
    if time != 0:
        if time >= 60:
            print(f"{(time // 60)}:{time % 60:0>2d} hours before the start")
        elif time < 60:
            print(f"{time} minutes before the start")
