x = float(input())
y = float(input())
h = float(input())

green_paint_per_liter = 3.4
red_paint_per_liter = 4.3
door_width = 1.2
door_height = 2
window_side = 1.5

side_wall_area = x * y
window_area = window_side * window_side
total_side_wall_area = (2 * side_wall_area) - (2 * window_area)
back_side = x * x
door_area = door_width * door_height
front_and_back_side = (2 * back_side) - door_area
total_wall_area = total_side_wall_area + front_and_back_side

total_green_paint = total_wall_area / green_paint_per_liter

print(f"{total_green_paint:.2f}")

two_rectangles = 2 * (x * y)
two_triangles = 2 * (x * h / 2)
total_roof_area = two_rectangles + two_triangles

total_red_paint = total_roof_area / red_paint_per_liter

print(f"{total_red_paint:.2f}")
