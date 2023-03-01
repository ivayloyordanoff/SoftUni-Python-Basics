best_player = ""
goals = 0
hat_trick = False

command = input()

while command != "END":
    current_player_name = command
    current_goals = int(input())

    if current_goals > goals:
        goals = current_goals
        best_player = current_player_name

    if goals >= 3:
        hat_trick = True

    if goals >= 10:
        break

    command = input()

print(f"{best_player} is the best player!")

if hat_trick:
    print(f"He has scored {goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals} goals.")
