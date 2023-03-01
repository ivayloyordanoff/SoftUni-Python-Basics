width = int(input())
length = int(input())
height = int(input())

total_volume = width * length * height
free_space = True

command = input()

while command != "Done":
    boxes_count = int(command)
    total_volume -= boxes_count

    if total_volume <= 0:
        free_space = False
        break

    command = input()

if free_space:
    print(f"{total_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")
