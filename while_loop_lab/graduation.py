name = input()

current_class = 1
total_grade = 0
excluded = False
bad_grade = 0

while current_class <= 12:
    current_grade = float(input())

    if current_grade < 4:
        bad_grade += 1

        if bad_grade == 2:
            excluded = True
            break

        continue

    current_class += 1
    total_grade += current_grade

if excluded:
    print(f"{name} has been excluded at {current_class} grade")
else:
    avg_grade = total_grade / 12
    print(f"{name} graduated. Average grade: {avg_grade:.2f}")
