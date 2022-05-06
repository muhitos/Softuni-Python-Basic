toy_price = 5
switcher_price = 15
toy_counter = 0
switcher_counter = 0

command = input()

while command != "Christmas":
    years_old = int(command)

    if years_old <= 16:
        toy_counter += 1
    else:
        switcher_counter += 1

    command = input()

print(f"Number ot adults: {switcher_counter}")
print(f"Number of kids: {toy_counter}")
print(f"Money for toys: {toy_counter * toy_price}")
print(f"Money for sweaters: {switcher_counter * switcher_price}")