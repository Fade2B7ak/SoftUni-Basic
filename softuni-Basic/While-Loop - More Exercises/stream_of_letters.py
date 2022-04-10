letter = input()

n_letter = False
o_letter = False
c_letter = False

prtint_line = ''
word = ''

while letter != 'End':
    fist_letter = input()
    second_letter = input()
    if fist_letter or second_letter:
        if letter == 'n':
            n_letter = True
            word += letter

        elif letter == 'o':
            o_letter = True
            word += letter

        elif letter == 'c':
            c_letter = True
            word += letter
        else:
            word += letter

    if n_letter and o_letter and c_letter:
        prtint_line += word
        n_letter = False
        o_letter = False
        c_letter = False

    letter = input()
print(letter)
