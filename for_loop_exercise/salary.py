tabs_count = int(input())
salary = int(input())

copy_salary = salary

for i in range(1, tabs_count + 1):
    name_web = input()

    if name_web == "Facebook":
        copy_salary -= 150
    elif name_web == "Instagram":
        copy_salary -= 100
    elif name_web == "Reddit":
        copy_salary -= 50
    if copy_salary <= 0:
        break

if copy_salary > 0:
    print(copy_salary)
else:
    print(f"You have lost your salary.")
