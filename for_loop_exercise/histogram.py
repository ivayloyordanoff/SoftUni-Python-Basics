n = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for i in range(1, n + 1):
    num = int(input())

    if num < 200:
        p1_count += 1
    elif num <= 399:
        p2_count += 1
    elif num <= 599:
        p3_count += 1
    elif num <= 799:
        p4_count += 1
    else:
        p5_count += 1

p1_percent = p1_count / n * 100
p2_percent = p2_count / n * 100
p3_percent = p3_count / n * 100
p4_percent = p4_count / n * 100
p5_percent = p5_count / n * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")
