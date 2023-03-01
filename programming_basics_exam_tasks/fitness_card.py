available_sum = float(input())
gender = input()
age = int(input())
sport = input()

money = 0

if gender == "m":
    if sport == "Gym":
        money = 42
    elif sport == "Boxing":
        money = 41
    elif sport == "Yoga":
        money = 45
    elif sport == "Zumba":
        money = 34
    elif sport == "Dances":
        money = 51
    elif sport == "Pilates":
        money = 39
elif gender == "f":
    if sport == "Gym":
        money = 35
    elif sport == "Boxing":
        money = 37
    elif sport == "Yoga":
        money = 42
    elif sport == "Zumba":
        money = 31
    elif sport == "Dances":
        money = 53
    elif sport == "Pilates":
        money = 37

if age <= 19:
    money *= 0.80

if available_sum >= money:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    diff = abs(available_sum - money)
    print(f"You don't have enough money! You need ${diff:.2f} more.")
