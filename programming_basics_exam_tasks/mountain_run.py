from math import floor

record_in_sec = float(input())
distance_in_meters = float(input())
time_in_sec_per_meter = float(input())

total_time_in_sec = distance_in_meters * time_in_sec_per_meter
delay = (floor(distance_in_meters / 50)) * 30

total_time = total_time_in_sec + delay

if total_time < record_in_sec:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    diff = abs(record_in_sec - total_time)
    print(f"No! He was {diff:.2f} seconds slower.")
