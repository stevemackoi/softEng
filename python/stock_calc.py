stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

num_shares = int(input())

stock_selections = []
for i in range(num_shares):
    stock = input()
    stock_selections.append(stock)

total_cost = 0.0
for stock in stock_selections:
    total_cost += stocks[stock]

print(f"Total price: ${total_cost:.2f}")
