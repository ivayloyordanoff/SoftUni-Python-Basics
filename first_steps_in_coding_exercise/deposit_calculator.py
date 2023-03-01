deposit_sum = float(input())
term_deposit = float(input())
annual_percent = float(input())

interest = (deposit_sum * annual_percent / 100) / 12
total_sum = deposit_sum + (term_deposit * interest)

print(total_sum)
