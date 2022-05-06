from math import pi

figure = input()
# създаваме глобална променлива"area" която да пази стойността
# на всички area's  който ще създадем.Вместо да пишем "print"
# на всеки изход :
area = 0

if figure == 'square':
    a = float(input())
    area = a * a  # формула квадрат

elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b  # формула правоъгълник

elif figure == 'circle':
    radius = float(input())
    area = pi * radius ** 2  # формула радиус на квадрат (**2).

elif figure == 'triangle':
    a = float(input())
    b = float(input())
    area = a * b / 2  # формула за триъгълник

print(f'{area:.3f}')
