k = int(input())
l = int(input())
m = int(input())
n = int(input())

count_subs = 0

for first in range(k, 8 + 1, + 1):
    for second in range(9, l - 1, - 1):
        for third in range(m, 8 + 1, + 1):
            for forth in range(9, n - 1, - 1):
                if first % 2 == 0 and third % 2 == 0 and second % 2 != 0 and forth % 2 != 0:
                    if first == third and second == forth:
                        print('Cannot change the same player.')
                    else:
                        print(f'{first}{second} - {third}{forth}')
                        count_subs += 1
                if count_subs == 6:
                    break
            if count_subs == 6:
                break
        if count_subs == 6:
            break
    if count_subs == 6:
        break