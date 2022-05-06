# Задача: 5 Годзила срещу Конг:

budget = float(input())
number_of_statist = int(input())
one_dress_price = float(input())

# Декорът за филма е на стойност 10% от бюджета.
decor = budget * 0.1  # или budget * 10/ 100
dress_price = number_of_statist * one_dress_price

if number_of_statist > 150:
    dress_price *= 0.9  # или dresses_price = dresses_price * 90 /100
    # вземи (0.9) 90% от текущата им стойност

needed_money = decor + dress_price

difference = abs(needed_money - budget)

if needed_money > budget:  # Парите не стигат
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")

else:  # Парите стигат -> budget >= needed_money
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
