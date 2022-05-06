import math

figure = input()
side_a = float(input())
# или area = 0 --->

if figure == 'square':
    area = side_a * side_a
    print(f"{area:.3f}")
elif figure == 'rectangle':
    side_b = float(input())
    area = side_a * side_b
    print(f'{area:.3f}')
elif figure == 'circle':
    area = math.pi * side_a * side_a  # радиуса на кръг
    # Или: area = pi * radius ** 2(радиус на (** 2)квадрат
    print(f'{area:.3f}')

elif figure == 'triangle':
    h = float(input())
    area = (side_a * h) / 2  # формула триъгълник
#ИЛИ:  a = float(input())
    # b = float(input())
    # a * b / 2
    print(f'{area:.3f}')
