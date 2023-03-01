chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = chrysanthemums_count * 2
    roses_price = roses_count * 4.10
    tulips_price = tulips_count * 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = chrysanthemums_count * 3.75
    roses_price = roses_count * 4.50
    tulips_price = tulips_count * 4.15

total_price = chrysanthemums_price + roses_price + tulips_price

if holiday == "Y":
    total_price *= 1.15

if tulips_count > 7 and season == "Spring":
    total_price *= 0.95

if roses_count >= 10 and season == "Winter":
    total_price *= 0.90

if chrysanthemums_count + roses_count + tulips_count > 20:
    total_price *= 0.80

total_price += 2

print(f"{total_price:.2f}")
