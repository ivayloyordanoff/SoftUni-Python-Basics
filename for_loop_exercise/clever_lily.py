age = int(input())
laundry_price = float(input())
toy_price = int(input())

toys_count = 0
money = 10
current_sum = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toys_count += 1
    else:
        current_sum += money - 1
        money += 10

money_toys = toy_price * toys_count
total_sum = money_toys + current_sum
diff = abs(total_sum - laundry_price)

if total_sum >= laundry_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
