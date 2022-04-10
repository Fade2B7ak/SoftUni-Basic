age = float(input())
type_of_gender = input()
if type_of_gender == 'm':
    if age >= 16:
        type_of_gender = "Mr."
    else:
        type_of_gender = "Master"
if type_of_gender == 'f':
    if age >= 16:
        type_of_gender = "Ms."
    else:
        type_of_gender ="Miss"
print(type_of_gender)