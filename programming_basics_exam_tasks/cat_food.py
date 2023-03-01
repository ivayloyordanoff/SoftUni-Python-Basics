cats_count = int(input())

price_per_kg_food = 12.45
first_group = 0
second_group = 0
third_group = 0
total_food_in_gr = 0

for days in range(cats_count):
    food = float(input())

    if 100 <= food < 200:
        first_group += 1
    elif 200 <= food < 300:
        second_group += 1
    elif 300 <= food < 400:
        third_group += 1

    total_food_in_gr += food

total_food = total_food_in_gr / 1000
food_price_per_day = total_food * price_per_kg_food

print(f"Group 1: {first_group} cats.")
print(f"Group 2: {second_group} cats.")
print(f"Group 3: {third_group} cats.")
print(f"Price for food per day: {food_price_per_day:.2f} lv.")
