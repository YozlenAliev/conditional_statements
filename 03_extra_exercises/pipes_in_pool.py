volume = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
worker_out_hours = float(input())

pipe_one = pipe_one_debit * worker_out_hours
pipe_two = pipe_two_debit * worker_out_hours
total_litres = pipe_one + pipe_two
total_percent_filled = (total_litres / volume) * 100
pipe_one_percent = (pipe_one / total_litres) * 100
pipe_two_percent = (pipe_two / total_litres) * 100

if total_litres <= volume:
    print(f'The pool is {total_percent_filled:.2f}% full. Pipe 1: {pipe_one_percent:.2f}%. Pipe 2: {pipe_two_percent:.2f}%.')

else:
    overflow = total_litres - volume
    print(f'For {worker_out_hours} hours the pool overflows with {overflow:.2f} liters.')
