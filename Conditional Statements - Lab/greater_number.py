first_num = int(input())
second_num = int(input())

if first_num > second_num:
    print(first_num)

else:
    print(second_num)

#други примери за извеждане:

a, b = int(input()), int(input())

print(a) if a > b else print(b)
