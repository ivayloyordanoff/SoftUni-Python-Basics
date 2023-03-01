budget = float(input())
statists = int(input())
clothes = float(input())

decor = budget * 0.10
sum_clothes = statists * clothes

if statists > 150:
    sum_clothes = sum_clothes * 0.90

current_sum = decor + sum_clothes
diff = abs(budget - current_sum)

if current_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
