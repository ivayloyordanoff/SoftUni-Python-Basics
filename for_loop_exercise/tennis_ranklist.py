from math import floor

tournaments_count = int(input())
init_points = int(input())

sum_points = 0
winner_tournaments_count = 0

for i in range(1, tournaments_count + 1):
    level = input()

    if level == "W":
        sum_points += 2000
        winner_tournaments_count += 1
    elif level == "F":
        sum_points += 1200
    elif level == "SF":
        sum_points += 720

final_points = init_points + sum_points
avg_points = sum_points / tournaments_count
winner_tournaments_percent = winner_tournaments_count / tournaments_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {floor(avg_points)}")
print(f"{winner_tournaments_percent:.2f}%")
