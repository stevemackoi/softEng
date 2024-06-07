current_price = int(input())
last_months_price = int(input())
diff = current_price - last_months_price
mortgage = (current_price * 0.051) / 12
print('This house is $' + str(current_price) + '. The change is $' + str(diff) + ' since last month.')
print('The estimated monthly mortgage is $' + str(f'{mortgage:.2f}') + '.')
