import math

name_futboll_player = input()
budget = float(input())
number_beer_botle = int(input())
number_chips = int(input())

beer = 1.20
chips = 0.55

total_price_beer = 1.20 * number_beer_botle
price_chips = total_price_beer - (total_price_beer * 0.55)

total_price_chips = math.ceil(price_chips * number_chips)

total_sum = total_price_beer + total_price_chips

diff = abs(total_sum - budget)

if total_sum <= budget:
    print(f"{name_futboll_player} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name_futboll_player} needs {diff:.2f} more leva!")


