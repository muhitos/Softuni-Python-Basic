deposit_amount = float(input())
months = int(input())
annual_rate = float(input())

# сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

per_year = deposit_amount * (annual_rate / 100)

per_month = per_year / 12

total_sum = deposit_amount + (months * per_month)

print(total_sum)
