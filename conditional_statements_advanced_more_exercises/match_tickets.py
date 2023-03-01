budget = float(input())
category = input()
count_people = int(input())

ticket_price = 0
transport_money = 0

if category == "VIP":
    ticket_price = count_people * 499.99
    if 1 <= count_people <= 4:
        transport_money = budget * 0.75
    elif 5 <= count_people <= 9:
        transport_money = budget * 0.60
    elif 10 <= count_people <= 24:
        transport_money = budget * 0.50
    elif 25 <= count_people <= 49:
        transport_money = budget * 0.40
    elif count_people >= 50:
        transport_money = budget * 0.25
elif category == "Normal":
    ticket_price = count_people * 249.99
    if 1 <= count_people <= 4:
        transport_money = budget * 0.75
    elif 5 <= count_people <= 9:
        transport_money = budget * 0.60
    elif 10 <= count_people <= 24:
        transport_money = budget * 0.50
    elif 25 <= count_people <= 49:
        transport_money = budget * 0.40
    elif count_people >= 50:
        transport_money = budget * 0.25

total_sum = ticket_price + transport_money
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
