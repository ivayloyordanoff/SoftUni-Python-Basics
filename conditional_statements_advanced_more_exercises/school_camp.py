season = input()
group_type = input()
count_students = int(input())
count_nights = int(input())

price_per_night = 0
sport = ""

if group_type == "boys" or group_type == "girls":
    if season == "Winter":
        price_per_night = 9.60
    elif season == "Spring":
        price_per_night = 7.20
    elif season == "Summer":
        price_per_night = 15
elif group_type == "mixed":
    if season == "Winter":
        price_per_night = 10
    elif season == "Spring":
        price_per_night = 9.50
    elif season == "Summer":
        price_per_night = 20

total_sum = count_students * price_per_night * count_nights

if count_students >= 50:
    total_sum *= 0.50
elif 20 <= count_students < 50:
    total_sum *= 0.85
elif 10 <= count_students < 20:
    total_sum *= 0.95

if group_type == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif group_type == "mixed":
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"

print(f"{sport} {total_sum:.2f} lv.")
