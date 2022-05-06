number_cats = int(input())
kg_food = 12.45

gp1 = 0
gp2 = 0
gp3 = 0
points = 0
total_food_for_all_cats = 0

for i in range(1, number_cats + 1):
    food_gr = int(input())
    total_food_for_all_cats += food_gr
    if 100 <= food_gr < 200:
        gp1 += 1
    elif 200 <= food_gr < 300:
        gp2 += 1
    elif 300 <= food_gr < 400:
        gp3 += 1

tot_tot = total_food_for_all_cats / 1000
price_food_for_one_day = tot_tot * kg_food

print(f"Group 1: {gp1} cats.")
print(f"Group 2: {gp2} cats.")
print(f"Group 3: {gp3} cats.")
print(f"Price for food per day: {price_food_for_one_day:.2f} lv.")



