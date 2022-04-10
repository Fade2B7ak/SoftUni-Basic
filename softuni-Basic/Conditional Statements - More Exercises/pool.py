obem_v = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

debit_pipe1 = pipe1 * hours
debit_pipe2 = pipe2 * hours
full_debit = debit_pipe1 + debit_pipe2

if obem_v >= full_debit:
    full_debit_in_percents = (full_debit * 100) / obem_v
    pipe1_percent = (debit_pipe1 * 100) / full_debit
    pipe2_percent = (debit_pipe2 * 100) / full_debit
    print(f"The pool is {full_debit_in_percents:.2f}% full. Pipe 1: {pipe1_percent:.2f}%. "
          f"Pipe 2: {pipe2_percent:.2f}%.")
else:
    overflow_amount = full_debit - obem_v
    print(f"For {hours} hours the pool overflows with {overflow_amount} liters.")
