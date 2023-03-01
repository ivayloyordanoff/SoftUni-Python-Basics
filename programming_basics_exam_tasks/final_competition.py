dancers_count = int(input())
points_count = float(input())
season = input()
place = input()

money_won = 0
expenses = 0

if place == "Bulgaria":
    money_won = dancers_count * points_count
elif place == "Abroad":
    money_won = dancers_count * points_count * 1.5

if place == "Bulgaria":
    if season == "summer":
        expenses = money_won * 0.05
    elif season == "winter":
        expenses = money_won * 0.08
elif place == "Abroad":
    if season == "summer":
        expenses = money_won * 0.10
    elif season == "winter":
        expenses = money_won * 0.15

money_after_expenses = money_won - expenses
charity = money_after_expenses * 0.75
total_money = money_after_expenses - charity
money_per_dancer = total_money / dancers_count

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
