#  a = int(input('a =  '))

#  area = a * a
#  print(area)
# -----------------------------
#  прости проверки -булеви променливи 'is_positive' във случая.
# is_positive  = True

# print(is_positive)
# ------------------------------------------------------
# import math

# a = float(input())

#  print (math.floor(a))
# --------------------------------------------
# # print(abs(50 -100)) - абсолютна стойност
# ----------------------------------------------
# print(round(a , 2 )) - Банкерско закръгляне
# ----------------------------------------------
# print('A' * 3 ** 2)
# a = 5
# b = 1000
# result = a / b

# print(result)
# --------------------------------------
# Принер за сравнение 'True' - 'False'

# budget = int(input())

# is_positive =  budget >= 5.50
# print(is_positive)
# ----------------------------------------

# user_input = input()
#
# if user_input == "s3cr3t!P@ssw0rd":
#     print('Welcome')
# else:
#     print('Wrong password!')
# -----------------------------------------
day_of_week = input()
salary = 0  # ---- важи в рамките на целия код!

if day_of_week == "Monday":
    salary = 1000  # ----> тази променлива ще бъде инициализирана
    # на '1000' само когато влезне във if- стейтмента
print(salary)
