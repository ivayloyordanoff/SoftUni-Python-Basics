count_km = int(input())
day_or_night = input()

taxi_start_price = 0.70
taxi_day_price = 0.79
taxi_night_price = 0.90
bus_price = 0.09
train_price = 0.06

cheap_transport = 0

if count_km < 20:
    cheap_transport += taxi_start_price
    if day_or_night == "day":
        cheap_transport += count_km * taxi_day_price
    elif day_or_night == "night":
        cheap_transport += count_km * taxi_night_price
elif count_km < 100:
    cheap_transport += bus_price * count_km
else:
    cheap_transport += train_price * count_km

print(f"{cheap_transport:.2f}")
