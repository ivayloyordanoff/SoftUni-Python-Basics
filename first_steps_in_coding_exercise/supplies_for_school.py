packages_pens = 5.80
packages_markers = 7.20
detergent_lt = 1.20

number_packages_pens = int(input())
number_packages_markers = int(input())
number_detergent_lt = int(input())
discount_percent = int(input()) / 100

sum_packages_pens = packages_pens * number_packages_pens
sum_packages_markers = packages_markers * number_packages_markers
sum_detergent_lt = detergent_lt * number_detergent_lt
sum_materials = sum_packages_pens + sum_packages_markers + sum_detergent_lt

final_price = sum_materials - (sum_materials * discount_percent)

print(final_price)
