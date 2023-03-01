price_for_kg_vegetables = float(input())
price_for_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

total_sum_in_lv = price_for_kg_vegetables * total_kg_vegetables \
                  + price_for_kg_fruits * total_kg_fruits

total_sum_in_euro = total_sum_in_lv / 1.94

print(f"{total_sum_in_euro:.2f}")
