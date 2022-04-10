import sys

max_number = - sys.maxsize
command = input()
while command != 'Stop':
    current_number = int(command)
    if current_number > max_number:
        max_number = current_number
    command = input()
if max_number != -sys.maxsize:
    print(max_number)