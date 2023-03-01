nylon = 1.50
paint = 14.50
thinner = 5.00

quantity_nylon = int(input())
quantity_paint = int(input())
quantity_thinner = int(input())
hours = int(input())

sum_nylon = (quantity_nylon + 2) * nylon
sum_paint = (quantity_paint + 0.10 * quantity_paint) * paint
sum_thinner = quantity_thinner * thinner
sum_bags = 0.40
sum_materials = sum_nylon + sum_paint + sum_thinner + sum_bags
sum_workers = (sum_materials * 0.30) * hours

final_price = sum_materials + sum_workers

print(final_price)
