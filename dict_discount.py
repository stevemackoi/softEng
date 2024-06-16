purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

item = input()
num = int(input())

if num < 10: #no discount
    low = (purchase[item] * num)
    print(item + " $" + str(f'{low:.2f}' ))
elif 9 < num < 21: #5% discount
    med = ((purchase[item] * num) * .95)
    print(item + " $" + str(f'{med:.2f}' ))
elif num > 20: #10% discount
    high = ((purchase[item] * num) * .90)
    print(item + " $" + str(f'{high:.2f}' ))
