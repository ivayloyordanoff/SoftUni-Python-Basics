from math import floor, ceil

count_days = int(input())
food_kg = int(input())
food_for_dog_kg = float(input())
food_for_cat_kg = float(input())
food_for_turtle_g = float(input())

food_for_turtle_kg = food_for_turtle_g / 1000
total_needed_food_kg = count_days * (food_for_dog_kg + food_for_cat_kg + food_for_turtle_kg)
diff = abs(food_kg - total_needed_food_kg)

if food_kg >= total_needed_food_kg:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
