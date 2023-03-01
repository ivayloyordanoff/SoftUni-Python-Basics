days_count = int(input())

liters = 0
degrees = 0

for day in range(days_count):
    current_liters = float(input())
    current_degrees = float(input())

    liters += current_liters
    degrees += current_liters * current_degrees

average_degrees = degrees / liters

print(f"Liter: {liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print(f"Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print(f"Super!")
else:
    print(f"Dilution with distilled water!")
