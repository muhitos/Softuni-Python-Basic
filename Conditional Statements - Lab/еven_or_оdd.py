number = int(input())

# num % 2 --> 10 %2 -> 10/2 = 5 - четно няма остатък
# или
# num % 2 --> 7 % 2 -> 7/2 = 3 - остатък 1

if number % 2 == 0:
    print('even')
else:
    print('odd')
