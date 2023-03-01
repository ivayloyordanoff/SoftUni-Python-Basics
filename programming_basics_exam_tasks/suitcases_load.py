capacity = float(input())

suitcases_counter = 0

while True:
    command = input()

    if command == "End":
        print(f"Congratulations! All suitcases are loaded!")
        break

    current_suitcase_volume = float(command)

    if capacity < current_suitcase_volume:
        print(f"No more space!")
        break

    suitcases_counter += 1

    if suitcases_counter % 3 == 0:
        current_suitcase_volume *= 1.10

    capacity -= current_suitcase_volume

print(f"Statistic: {suitcases_counter} suitcases loaded.")
