maiden_party_price = float(input())
love_letters_count = int(input())
wax_roses_count = int(input())
keychains_count = int(input())
caricatures_count = int(input())
luck_count = int(input())

love_letter_price = 0.60
wax_rose_price = 7.20
keychain_price = 3.60
caricature_price = 18.20
luck_price = 22

total_sum = love_letters_count * love_letter_price \
            + wax_roses_count * wax_rose_price \
            + keychains_count * keychain_price \
            + caricatures_count * caricature_price \
            + luck_count * luck_price

items_count = love_letters_count + wax_roses_count + keychains_count + caricatures_count + luck_count

if items_count > 25:
    total_sum -= total_sum * 0.35

final_sum = total_sum * 0.90
diff = abs(final_sum - maiden_party_price)

if final_sum > maiden_party_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
