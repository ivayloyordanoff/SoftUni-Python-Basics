budget = float(input())
season = input()

destination = ""
rest = ""
spent_sum = 0

if season == "summer":
    rest = "Camp"
elif season == "winter":
    rest = "Hotel"

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        spent_sum = budget * 0.30
    elif season == "winter":
        spent_sum = budget * 0.70

elif budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        spent_sum = budget * 0.40
    elif season == "winter":
        spent_sum = budget * 0.80

if budget > 1000:
    destination = "Europe"
    rest = "Hotel"
    spent_sum = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{rest} - {spent_sum:.2f}")
