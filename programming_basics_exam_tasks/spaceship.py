width_of_spaceship = float(input())
length_of_spaceship = float(input())
height_of_spaceship = float(input())
average_height_of_astronaut = float(input())

volume_of_spaceship = width_of_spaceship * length_of_spaceship * height_of_spaceship
volume_of_one_room = (average_height_of_astronaut + 0.40) * 2 * 2
astronauts_count = int(volume_of_spaceship / volume_of_one_room)

if 3 <= astronauts_count <= 10:
    print(f"The spacecraft holds {astronauts_count} astronauts.")
elif astronauts_count < 3:
    print(f"The spacecraft is too small.")
elif astronauts_count > 10:
    print(f"The spacecraft is too big.")
