from math import floor, ceil

count_magnolias = int(input())
count_hyacinths = int(input())
count_roses = int(input())
count_cacti = int(input())
gift_price = float(input())

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.50
cacti_price = 8

total_price = count_magnolias * magnolias_price \
              + count_hyacinths * hyacinths_price \
              + count_roses * roses_price \
              + count_cacti * cacti_price
total_price_after_tax = total_price * 0.95

diff = abs(total_price_after_tax - gift_price)

if total_price_after_tax >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")
