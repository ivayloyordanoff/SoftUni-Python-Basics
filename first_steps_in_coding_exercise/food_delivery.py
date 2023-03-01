chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15

number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())

sum_chicken_menu = number_chicken_menu * chicken_menu
sum_fish_menu = number_fish_menu * fish_menu
sum_vegetarian_menu = number_vegetarian_menu * vegetarian_menu
sum_menu = sum_chicken_menu + sum_fish_menu + sum_vegetarian_menu
desert_price = 0.20 * sum_menu

final_price = sum_menu + desert_price + 2.50

print(final_price)
