count_of_students = int(input())

average_sum = 0
fail_score_counter = 0
average_score_counter = 0
good_score_counter = 0
top_score_counter = 0

for students in range(count_of_students):
    grade = float(input())
    average_sum += grade
    if 2 <= grade <= 2.99:
        fail_score_counter += 1
    elif 3 <= grade <= 3.99:
        average_score_counter += 1
    elif 4 <= grade <= 4.99:
        good_score_counter += 1
    elif 5 <= grade <= 6:
        top_score_counter += 1

print(f'Top students: {top_score_counter / count_of_students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {good_score_counter / count_of_students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {average_score_counter / count_of_students * 100:.2f}%')
print(f'Fail: {fail_score_counter / count_of_students * 100:.2f}%')
print(f'Average: {average_sum / count_of_students:.2f}')