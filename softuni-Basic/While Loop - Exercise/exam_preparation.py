count_of_bad_grades = int(input())

probles_count = 0
problems_sum = 0
poor_grades = 0
has_passed = True
last_problem = ''

problem_name = input()

while problem_name != 'Enough':
    last_problem = problem_name
    grade = float(input())
    probles_count += 1
    problems_sum += grade

    if grade <= 4:
        poor_grades += 1
        if poor_grades == count_of_bad_grades:
            print(f'You need a break, {count_of_bad_grades} poor grades.')
            has_passed = False
            break
    problem_name = input()

if has_passed:
    print(f'Average score: {problems_sum / probles_count:.2f}')
    print(f'Number of problems: {probles_count}')
    print(f'Last problem: {last_problem}')