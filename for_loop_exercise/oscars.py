actor_name = input()
init_points = float(input())
count_people = int(input())

total_points = init_points

for i in range(1, count_people + 1):
    name = input()
    current_points = float(input())

    points = (len(name) * current_points) / 2
    total_points += points

    if total_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points < 1250.5:
    needed_points = abs(1250.5 - total_points)
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
