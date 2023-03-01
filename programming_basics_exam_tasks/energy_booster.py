fruit = input()
size_of_set = input()
count_sets = int(input())

price = 0

if fruit == "Watermelon":
    if size_of_set == "small":
        price = 2 * 56 * count_sets
    elif size_of_set == "big":
        price = 5 * 28.70 * count_sets
elif fruit == "Mango":
    if size_of_set == "small":
        price = 2 * 36.66 * count_sets
    elif size_of_set == "big":
        price = 5 * 19.60 * count_sets
elif fruit == "Pineapple":
    if size_of_set == "small":
        price = 2 * 42.10 * count_sets
    elif size_of_set == "big":
        price = 5 * 24.80 * count_sets
elif fruit == "Raspberry":
    if size_of_set == "small":
        price = 2 * 20 * count_sets
    elif size_of_set == "big":
        price = 5 * 15.20 * count_sets

if 400 <= price <= 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.50

print(f"{price:.2f} lv.")
