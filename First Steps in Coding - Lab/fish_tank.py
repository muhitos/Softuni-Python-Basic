lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = lenght * width * height

total_lt = volume / 1000
percent_lt = total_lt * (percent / 100)

needed_lt = total_lt - percent_lt

print(needed_lt)
