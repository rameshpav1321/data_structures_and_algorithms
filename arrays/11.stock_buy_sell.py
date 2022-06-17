def stock_buy_sell(lst):
    profit = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            profit += lst[i]-lst[i-1]
    return profit


print(stock_buy_sell([1, 5, 3, 8, 12]))
