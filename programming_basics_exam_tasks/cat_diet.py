fats_percent = int(input())
proteins_percent = int(input())
carbohydrates_percent = int(input())
total_count_calories = int(input())
water_percent = int(input())

calories_per_fats_gr = 9
calories_per_proteins_gr = 4
calories_per_carbohydrates_gr = 4

total_gr_fats = (fats_percent / 100) * total_count_calories / calories_per_fats_gr
total_gr_proteins = (proteins_percent / 100) * total_count_calories / calories_per_proteins_gr
total_gr_carbohydrates = (carbohydrates_percent / 100) * total_count_calories / calories_per_carbohydrates_gr

total_food_gr = total_gr_fats + total_gr_proteins + total_gr_carbohydrates
calories_per_gr_food = total_count_calories / total_food_gr
calories = calories_per_gr_food - (water_percent / 100 * calories_per_gr_food)

print(f"{calories:.4f}")
