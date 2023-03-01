type_flowers = input()
number_flowers = int(input())
budget = int(input())

total_sum = 0

if type_flowers == "Roses":
    total_sum = number_flowers * 5

    if number_flowers > 80:
        total_sum *= 0.90

if type_flowers == "Dahlias":
    total_sum = number_flowers * 3.80

    if number_flowers > 90:
        total_sum *= 0.85

if type_flowers == "Tulips":
    total_sum = number_flowers * 2.80

    if number_flowers > 80:
        total_sum *= 0.85

if type_flowers == "Narcissus":
    total_sum = number_flowers * 3

    if number_flowers < 120:
        total_sum *= 1.15

if type_flowers == "Gladiolus":
    total_sum = number_flowers * 2.50

    if number_flowers < 80:
        total_sum *= 1.20

diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
