count_of_numebers = int(input())
odd_sum = 0
even_sum = 0

for possition in range(count_of_numebers):
    current_number = int(input())
    if possition % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {abs(odd_sum - even_sum)}")