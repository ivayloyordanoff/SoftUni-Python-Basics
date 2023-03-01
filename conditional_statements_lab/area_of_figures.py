from math import pi

figure = input()

result = 0

if figure == 'square':
    side = float(input())
    result = side * side
elif figure == 'rectangle':
    side_1 = float(input())
    side_2 = float(input())
    result = side_1 * side_2
elif figure == 'circle':
    radius = float(input())
    result = radius ** 2 * pi
elif figure == 'triangle':
    side = float(input())
    height = float(input())
    result = side * height / 2

print(f'{result:.3f}')
