number_of_open_tabs = int(input())
salary = float(input())
condition = False

for _ in range (number_of_open_tabs):
    current_open_tan = input()

    if current_open_tan == 'Facebook':
        salary -= 150
    elif current_open_tan == 'Instagram':
        salary -= 100
    elif current_open_tan == 'Reddit':
        salary -= 50

    if salary <= 0:
        condition = True
        break

if not condition:
        print(int(salary))
else:
        print('You have lost our salary')

