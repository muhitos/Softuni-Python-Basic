# вариант 1:
for num in range(7, 1001, 10):
    print(num)

# вариант  2:

for num in range(1, 1001):
    if num % 10 == 7:  # Едно число завършва на 7, когато резултатът от модулното деление на числото и 10 е равен на 7;
        print(num)
