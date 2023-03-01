floors = int(input())
rooms = int(input())

flat_name = ""

for current_floor in range(floors, 0, -1):
    for current_room in range(rooms):
        if current_floor == floors:
            flat_name = "L"
        elif current_floor % 2 == 0:
            flat_name = "O"
        elif current_floor % 2 != 0:
            flat_name = "A"

        print(f"{flat_name}{current_floor}{current_room}", end=" ")

    print()
