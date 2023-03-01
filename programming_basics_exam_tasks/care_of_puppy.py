total_food_kg = int(input())

total_food_g = total_food_kg * 1000

command = input()

while command != "Adopted":
    current_food = int(command)
    total_food_g -= current_food

    command = input()

if total_food_g >= 0:
    print(f"Food is enough! Leftovers: {total_food_g} grams.")
else:
    print(f"Food is not enough. You need {abs(total_food_g)} grams more.")
