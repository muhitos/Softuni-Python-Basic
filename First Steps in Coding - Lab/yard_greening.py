square_meter = float(input())

total_price = square_meter * 7.61

discount = total_price * 0.18

total_price_discount = total_price - discount

print(f'The final price is: {total_price - discount}')
print(f'The discount is : {discount}')
