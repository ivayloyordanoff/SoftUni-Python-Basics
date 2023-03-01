number_of_jury = int(input())

presentation_number = 0
average_grade = 0

command = input()

while command != "Finish":
    current_presentation_name = command
    presentation_number += 1
    current_presentation_grade = 0

    for presentation_grade in range(number_of_jury):
        current_grade = float(input())
        current_presentation_grade += current_grade

    current_presentation_grade /= number_of_jury
    print(f"{current_presentation_name} - {current_presentation_grade:.2f}.")
    average_grade += current_presentation_grade

    command = input()

average_grade /= presentation_number

print(f"Student's final assessment is {average_grade:.2f}.")
