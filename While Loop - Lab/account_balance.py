# Някаква команда --> сума за внасяне(под формата на текст) или "NoMoreMoney"
command = input()
# повтаряме : четем сума +  проверка < 0
# спираме : command == "NoMoreMoney"
# продължаваме: command != "NoMoreMoney"
total_money = 0
while command != "NoMoreMoney":
    # command --> сума за вноска
    sum_income = float(command)
    if sum_income < 0:
        print('Invalid operation')
        break
    else:
        print(f"Increase: {sum_income:.2f}")
        total_money += sum_income
    command = input()
print(f"Total: {total_money:.2f}")