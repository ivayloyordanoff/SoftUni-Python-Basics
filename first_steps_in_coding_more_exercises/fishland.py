mackerel_price_kg = float(input())
sprat_price_kg = float(input())
bonito_kg = float(input())
scad_kg = float(input())
mussels_kg = float(input())

bonito_price_kg = mackerel_price_kg * 1.6
scad_price_kg = sprat_price_kg * 1.8
mussels_price_kg = 7.50

bonito_price = bonito_kg * bonito_price_kg
scad_price = scad_kg * scad_price_kg
mussels_price = mussels_kg * mussels_price_kg

total_price = bonito_price + scad_price + mussels_price

print(f"{total_price:.2f}")
