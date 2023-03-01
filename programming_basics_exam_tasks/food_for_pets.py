count_days = int(input())
quantity_food = float(input())

dog_food = 0
cat_food = 0
biscuits = 0

for days in range(1, count_days + 1):
    current_dog_food = int(input())
    current_cat_food = int(input())

    dog_food += current_dog_food
    cat_food += current_cat_food

    if days % 3 == 0:
        biscuits += (current_dog_food + current_cat_food) * 0.10

total_food = dog_food + cat_food
eaten_food_percent = total_food / quantity_food * 100
eaten_food_dog_percent = dog_food / total_food * 100
eaten_food_cat_percent = cat_food / total_food * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{eaten_food_percent:.2f}% of the food has been eaten.")
print(f"{eaten_food_dog_percent:.2f}% eaten from the dog.")
print(f"{eaten_food_cat_percent:.2f}% eaten from the cat.")
