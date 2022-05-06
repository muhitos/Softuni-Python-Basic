price_for_shirt = float(input())
sum = float(input())

price_for_shorts = price_for_shirt * 0.75
price_for_socks = price_for_shorts * 0.20
price_for_boots = (price_for_shirt + price_for_shorts ) * 2
total_sum = price_for_shirt + price_for_shorts + price_for_socks + price_for_boots
discount = total_sum * 0.85



if total_sum >= sum:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {discount:.2f} lv.")
else:
    diff = abs(sum - discount)
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")