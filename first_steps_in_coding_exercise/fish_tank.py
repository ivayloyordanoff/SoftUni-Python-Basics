length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

capacity = length * width * height / 1000
needed_lt = capacity * (1 - percent)

print(needed_lt)
