count_bitcoin = int(input())
count_yuan = float(input())
commission = float(input())

bitcoin_price_in_lv = 1168
yuan_price_in_usd = 0.15
usd_price_in_lv = 1.76
euro_price_in_lv = 1.95

yuan_price_in_lv = yuan_price_in_usd * usd_price_in_lv
total_sum_in_lv = count_bitcoin * bitcoin_price_in_lv + count_yuan * yuan_price_in_lv
total_sum_in_euro = total_sum_in_lv / euro_price_in_lv
commission_price = commission / 100 * total_sum_in_euro

final_price = total_sum_in_euro - commission_price

print(f"{final_price:.2f}")
