failed_grades = int(input())

failed_times_count = 0
solved_problems = 0
grades_sum = 0

last_problem = ""
has_failed = False

while failed_times_count < failed_grades:
    problem_name = input()

    if problem_name == "Enough":
        break

    grade = int(input())

    if grade <= 4:
        failed_times_count += 1

        if failed_times_count == failed_grades:
            has_failed = True
            break

    grades_sum += grade
    solved_problems += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {failed_grades} poor grades.")
else:
    avg_grade = grades_sum / solved_problems
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_problem}")
