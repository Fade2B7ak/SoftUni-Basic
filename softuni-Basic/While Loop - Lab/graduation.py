student_name = input()
bad_tries = 0
current_class = 1
grade = 0
is_ejected = False
while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_tries += 1
        if bad_tries == 2:
            is_ejected = True
            break
        continue
    grade += current_grade
    current_class += 1
if is_ejected:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")