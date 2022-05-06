futboll_team = input()
souvenir = input()
number_souvenir = int(input())

price = 0
condition = True # булева променлива започва със TRUE

if souvenir == "flags" and futboll_team == "Argentina":
    price = number_souvenir * 3.25
    print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")
elif souvenir == "caps" and futboll_team == "Argentina":
    price = number_souvenir * 7.20
    print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")
elif souvenir == "posters" and futboll_team == "Argentina":
    price = number_souvenir * 5.10
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")
elif souvenir == "stickers" and futboll_team == "Argentina":
    price = number_souvenir * 1.25
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")

if souvenir == "flags" and futboll_team == "Brazil":
    price = number_souvenir * 4.20
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")
elif souvenir == "caps" and futboll_team == "Brazil":
    price = number_souvenir * 8.50
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")
elif souvenir == "posters" and futboll_team == "Brazil":
    price = number_souvenir * 5.35
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")
elif souvenir == "stickers" and futboll_team == "Brazil":
    price = number_souvenir * 1.20
# print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")

if souvenir == "flags" and futboll_team == "Croatia":
    price = number_souvenir * 2.75
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")
elif souvenir == "caps" and futboll_team == "Croatia":
    price = number_souvenir * 6.90
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")
elif souvenir == "posters" and futboll_team == "Croatia":
    price = number_souvenir * 4.95
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")
elif souvenir == "stickers" and futboll_team == "Croatia":
    price = number_souvenir * 1.10
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")

if souvenir == "flags" and futboll_team == "Denmark":
    price = number_souvenir * 3.10
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")

elif souvenir == "caps" and futboll_team == "Denmark":
    price = number_souvenir * 6.50
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")

elif souvenir == "posters" and futboll_team == "Denmark":
    price = number_souvenir * 4.80
    # print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")
elif souvenir == "stickers" and futboll_team == "Denmark":
    price = number_souvenir * 0.90


elif futboll_team != 'Argentina' and futboll_team != 'Brazil' and futboll_team != 'Croatia' and futboll_team != \
        'Denmark':
    print("Invalid country!")
    condition = False # булева променлива грешен False

elif souvenir != "flags" and souvenir != "caps" and souvenir != "posters" and souvenir != "stickers":
    print("Invalid stock!")
    condition = False # отново грешен изход False

if condition: # Aкo condition ,не е бил променен някъде на False изпълни -(принта):
    print(f"Pepi bought {number_souvenir} {souvenir} of {futboll_team} for {price:.2f} lv.")
