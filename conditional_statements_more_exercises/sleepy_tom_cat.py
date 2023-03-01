rest_days = int(input())

norm_minutes_per_year = 30000
working_day_minutes = 63
rest_day_minutes = 127
working_days = 365 - rest_days
total_time = working_days * working_day_minutes + rest_days * rest_day_minutes
diff = abs(norm_minutes_per_year - total_time)
hours = diff // 60
minutes = diff % 60

if total_time > norm_minutes_per_year:
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
