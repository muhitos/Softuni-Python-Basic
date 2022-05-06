pens_count = int(input())  # Брой пакети химикали - цяло число в интервала
markers_count = int(input())  # Брой пакети маркери - цяло число в интервала
detergent_lt = int(input())  # Литри препарат за почистване на дъска -цяло число в интервала
percent = int(input())  # Процент намаление - цяло число в интервала

price_pens = pens_count * 5.80
price_markers = markers_count * 7.20
price_detergent = detergent_lt * 1.20

total_price = price_pens + price_markers + price_detergent

final_price = total_price - (total_price * (percent / 100))  # цяла цена + процент намаление

print(final_price)
