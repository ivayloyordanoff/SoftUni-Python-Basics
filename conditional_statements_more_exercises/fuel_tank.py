type_fuel = input()
liters_fuel = float(input())

if type_fuel == "Diesel":
    if liters_fuel >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")
elif type_fuel == "Gasoline":
    if liters_fuel >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")
elif type_fuel == "Gas":
    if liters_fuel >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")
else:
    print(f"Invalid fuel!")
