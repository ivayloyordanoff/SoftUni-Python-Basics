height = float(input())
width = float(input())

width = width * 100 - 100
height = height * 100
rows = height // 120
columns = width // 70

free_places = rows * columns
free_places = free_places - 1 - 2

print(int(free_places))
