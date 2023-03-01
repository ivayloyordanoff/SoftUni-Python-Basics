count_juniors = int(input())
count_seniors = int(input())
type_route = input()

tax_juniors = 0
tax_seniors = 0

if type_route == "trail":
    tax_juniors = count_juniors * 5.50
    tax_seniors = count_seniors * 7
elif type_route == "cross-country":
    tax_juniors = count_juniors * 8
    tax_seniors = count_seniors * 9.50
    if count_juniors + count_seniors >= 50:
        tax_juniors *= 0.75
        tax_seniors *= 0.75
elif type_route == "downhill":
    tax_juniors = count_juniors * 12.25
    tax_seniors = count_seniors * 13.75
elif type_route == "road":
    tax_juniors = count_juniors * 20
    tax_seniors = count_seniors * 21.50

total_sum = (tax_juniors + tax_seniors) * 0.95

print(f"{total_sum:.2f}")
