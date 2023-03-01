budget = float(input())
video_cards_count = int(input())
proc_count = int(input())
ram_count = int(input())

video_cards_sum = video_cards_count * 250
proc_sum = video_cards_sum * 0.35 * proc_count
ram_sum = video_cards_sum * 0.10 * ram_count
total_sum = video_cards_sum + proc_sum + ram_sum

if video_cards_count > proc_count:
    total_sum = total_sum * 0.85

diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
