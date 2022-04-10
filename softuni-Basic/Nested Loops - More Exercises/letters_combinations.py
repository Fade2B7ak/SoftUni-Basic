first_letter = input()
second_letter = input()
third_letter = input()

count = 0
alphabets = (first_letter, second_letter, third_letter)

for alpha1 in range(ord(first_letter), ord(second_letter) + 1):
    for alpha2 in range(ord(first_letter), ord(second_letter) + 1):
        for alpha3 in range(ord(first_letter), ord(second_letter) + 1):
            if alpha1 != ord(third_letter) and alpha2 != ord(third_letter) and alpha3 != ord(third_letter):

                count += 1

                print(f'{chr(alpha1)}{chr(alpha3)}{chr(alpha2)}', end=" ")
print(count)