#Прочитане на вход ,както следва реално число,цяло число,реално .
deposit = float(input())
months =  int(input())
annual_interest_percent = float(input())
#помощна променлива ,колко ще се получи за 1 год. със лихвен процент умножен по 100
annual_interest_percent = deposit * annual_interest_percent / 100
#Пресмятане на месечен
monthly_interest = annual_interest_percent /12
#Колко се полага
total_sum = deposit + months * monthly_interest

print(total_sum)