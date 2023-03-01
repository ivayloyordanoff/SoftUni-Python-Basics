type_fuel = input()
quantity_fuel = float(input())
club_card = input()

gasoline_price_per_liter = 2.22
diesel_price_per_liter = 2.33
gas_price_per_liter = 0.93
total_price = 0

if club_card == "Yes":
    gasoline_price_per_liter -= 0.18
    diesel_price_per_liter -= 0.12
    gas_price_per_liter -= 0.08

if type_fuel == "Gasoline":
    total_price = gasoline_price_per_liter * quantity_fuel
elif type_fuel == "Diesel":
    total_price = diesel_price_per_liter * quantity_fuel
elif type_fuel == "Gas":
    total_price = gas_price_per_liter * quantity_fuel

if 20 <= quantity_fuel <= 25:
    total_price *= 0.92
elif quantity_fuel > 25:
    total_price *= 0.90

print(f"{total_price:.2f} lv.")
