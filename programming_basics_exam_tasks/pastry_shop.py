sweet = input()
count_sweet = int(input())
day = int(input())

price = 0

if day <= 15:
    if sweet == "Cake":
        price = 24
    elif sweet == "Souffle":
        price = 6.66
    elif sweet == "Baklava":
        price = 12.60
elif day > 15:
    if sweet == "Cake":
        price = 28.70
    elif sweet == "Souffle":
        price = 9.80
    elif sweet == "Baklava":
        price = 16.98

total_price = count_sweet * price

if day <= 22:
    if 100 <= total_price <= 200:
        total_price *= 0.85
    elif total_price > 200:
        total_price *= 0.75
    if day <= 15:
        total_price *= 0.90

print(f"{total_price:.2f}")
