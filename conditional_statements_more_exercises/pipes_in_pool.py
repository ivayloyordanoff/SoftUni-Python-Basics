pool_volume = int(input())
pipe_one_per_hour = int(input())
pipe_two_per_hour = int(input())
hours = float(input())

pipe_one_volume = pipe_one_per_hour * hours
pipe_two_volume = pipe_two_per_hour * hours
total_volume = pipe_one_volume + pipe_two_volume
total_vol_percent = total_volume / pool_volume * 100
pipe_one_percent = pipe_one_volume / total_volume * 100
pipe_two_percent = pipe_two_volume / total_volume * 100

if total_volume <= pool_volume:
    print(
        f"The pool is {total_vol_percent:.2f}% full. Pipe 1: {pipe_one_percent:.2f}%. Pipe 2: {pipe_two_percent:.2f}%.")
else:
    diff = abs(total_volume - pool_volume)
    print(f"For {hours} hours the pool overflows with {diff:.2f} liters.")
