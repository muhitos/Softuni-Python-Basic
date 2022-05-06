number_chiken_menu = int(input())
number_fish_menu = int(input())
number_vegan_menu = int(input())


price_chiken = number_chiken_menu * 10.35
price_fish = number_fish_menu * 12.40
price_vegan = number_vegan_menu * 8.15

total_price_menu = price_chiken + price_fish + price_vegan

desert = 0.20 * total_price_menu

total_price_for_order = total_price_menu + desert + 2.50

print(total_price_for_order)