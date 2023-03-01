locations_count = int(input())

mined_gold = 0
average_gold_per_day = 0

for location in range(locations_count):
    expected_average_gold_per_day = float(input())
    current_days = int(input())

    for day in range(current_days):
        current_gold_per_day = float(input())

        mined_gold += current_gold_per_day
        average_gold_per_day = mined_gold / current_days

    if average_gold_per_day >= expected_average_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
        average_gold_per_day = 0
        mined_gold = 0
    else:
        print(f"You need {abs(expected_average_gold_per_day - average_gold_per_day):.2f} gold.")
        average_gold_per_day = 0
        mined_gold = 0
