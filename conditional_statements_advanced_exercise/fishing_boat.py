budget = int(input())
season = input()
number_fishers = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if number_fishers <= 6:
    boat_rent *= 0.90
elif 7 <= number_fishers <= 11:
    boat_rent *= 0.85
elif number_fishers >= 12:
    boat_rent *= 0.75

if number_fishers % 2 == 0:
    if not season == "Autumn":
        boat_rent *= 0.95

diff = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
