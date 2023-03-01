from math import ceil

average_speed = float(input())
needed_liters_per_100_km = float(input())

time_on_moon = 3

distance_between_moon_and_earth = 384400
total_distance = distance_between_moon_and_earth * 2
time = ceil(total_distance / average_speed)

total_time = time + time_on_moon
fuel = (needed_liters_per_100_km * total_distance) / 100

print(total_time)
print(f"{fuel:.0f}")
