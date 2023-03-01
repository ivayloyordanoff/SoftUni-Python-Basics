minutes_walk_per_day = int(input())
count_walk_per_day = int(input())
calories_per_day = int(input())

calories_per_minute = 5

total_calories = count_walk_per_day * minutes_walk_per_day * calories_per_minute

if total_calories >= calories_per_day * 0.5:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories}.")
