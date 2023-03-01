days_for_stay = int(input())
type_room = input()
rating = input()

sum_per_night = 0
total_sum = 0

if type_room == "room for one person":
    sum_per_night = 18
    total_sum = (days_for_stay - 1) * sum_per_night

elif type_room == "apartment":
    sum_per_night = 25

    if days_for_stay < 10:
        total_sum = (days_for_stay - 1) * sum_per_night * 0.70
    elif days_for_stay < 15:
        total_sum = (days_for_stay - 1) * sum_per_night * 0.65
    else:
        total_sum = (days_for_stay - 1) * sum_per_night * 0.50

elif type_room == "president apartment":
    sum_per_night = 35

    if days_for_stay < 10:
        total_sum = (days_for_stay - 1) * sum_per_night * 0.90
    elif days_for_stay < 15:
        total_sum = (days_for_stay - 1) * sum_per_night * 0.85
    else:
        total_sum = (days_for_stay - 1) * sum_per_night * 0.80

if rating == "positive":
    total_sum *= 1.25
elif rating == "negative":
    total_sum *= 0.90

print(f"{total_sum:.2f}")
