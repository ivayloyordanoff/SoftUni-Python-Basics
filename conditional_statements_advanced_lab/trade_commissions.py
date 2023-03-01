city = input()
sales = float(input())

city_is_valid = True
sales_is_valid = True

commission = 0

if 0 <= sales <= 500:
    if city == "Sofia":
        commission = 0.05
    elif city == "Varna":
        commission = 0.045
    elif city == "Plovdiv":
        commission = 0.055
    else:
        city_is_valid = False
elif 500 < sales <= 1000:
    if city == "Sofia":
        commission = 0.07
    elif city == "Varna":
        commission = 0.075
    elif city == "Plovdiv":
        commission = 0.08
    else:
        city_is_valid = False
elif 1000 < sales <= 10000:
    if city == "Sofia":
        commission = 0.08
    elif city == "Varna":
        commission = 0.10
    elif city == "Plovdiv":
        commission = 0.12
    else:
        city_is_valid = False
elif sales > 1000:
    if city == "Sofia":
        commission = 0.12
    elif city == "Varna":
        commission = 0.13
    elif city == "Plovdiv":
        commission = 0.145
    else:
        city_is_valid = False
else:
    sales_is_valid = False

final_price = sales * commission

if city_is_valid and sales_is_valid:
    print(f"{final_price:.2f}")
else:
    print("error")
