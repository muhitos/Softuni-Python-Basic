budget = float(input())
number_vc = int(input())
number_pr = int(input())
number_ram = int(input())

#Сума за видеокарти: 2 * 250 = 500 лв.
price_vc = number_vc * 250

#Цената за процесор: 35% от 500 = 175 лв.
#Сума за процесори: 1 * 175 = 175 лв.
price_pr = number_pr * (price_vc * 0.35)
# Цената за рам памет: 10% от 500 = 50 лв.
# Сума за рам памет: 3 * 50 = 150 лв.
price_ram = number_ram * (price_vc * 0.10)

# Обща сума: 500 + 175 + 150 = 825 лв.
sum = price_vc + price_pr + price_ram

# крайната цена: 825 – 15% = 701.25 лв.
discount = sum * 0.15

if number_vc > number_pr:
    end_sum = sum - discount
else:
    end_sum = sum

difference = abs(end_sum - budget)

if end_sum <= budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
