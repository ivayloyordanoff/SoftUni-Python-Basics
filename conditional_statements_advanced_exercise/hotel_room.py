month = input()
number_of_nights = int(input())

price_per_night_apartment = 0
price_per_night_studio = 0
total_sum_apartment = 0
total_sum_studio = 0

if month == "May" or month == "October":
    price_per_night_studio = 50
    price_per_night_apartment = 65

    if number_of_nights > 14:
        price_per_night_studio *= 0.70
    elif number_of_nights > 7:
        price_per_night_studio *= 0.95

elif month == "June" or month == "September":
    price_per_night_studio = 75.20
    price_per_night_apartment = 68.70

    if number_of_nights > 14:
        price_per_night_studio *= 0.80

elif month == "July" or month == "August":
    price_per_night_studio = 76
    price_per_night_apartment = 77

if number_of_nights > 14:
    price_per_night_apartment *= 0.90

total_sum_apartment = number_of_nights * price_per_night_apartment
total_sum_studio = number_of_nights * price_per_night_studio

print(f"Apartment: {total_sum_apartment:.2f} lv.")
print(f"Studio: {total_sum_studio:.2f} lv.")
