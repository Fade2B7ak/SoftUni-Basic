import string

word = ''
password = ''
c_letter = 0
o_letter = 0
n_letter = 0
letter = input()

while letter != 'End':
    if letter in string.ascii_lowercase or letter in string.ascii_uppercase:
        if letter == 'c' and c_letter == 0:
            c_letter += 1
        elif letter == 'c' and c_letter == 1:
            word += letter
        elif letter == 'o' and o_letter == 0:
            o_letter += 1
        elif letter == 'o' and o_letter == 1:
            word += letter
        elif letter == 'n' and n_letter == 0:
            n_letter += 1
        elif letter == 'n' and n_letter == 1:
            word += letter
        else:
            word += letter

        if c_letter == 1 and o_letter == 1 and n_letter == 1:
            word += ' '
            c_letter = 0
            o_letter = 0
            n_letter = 0
            password = word

    letter = input()
print(password)