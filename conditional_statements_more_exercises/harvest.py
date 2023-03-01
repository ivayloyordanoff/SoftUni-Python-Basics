from math import floor, ceil

square_meters = int(input())
grapes_per_one_square_meter = float(input())
needed_liters_wine = int(input())
count_workers = int(input())

total_grapes = square_meters * grapes_per_one_square_meter
wine = total_grapes * 0.40 / 2.5
diff = abs(wine - needed_liters_wine)

if wine < needed_liters_wine:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
else:
    remainder = diff / count_workers
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(remainder)} liters per person.")
