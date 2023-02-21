total = 0
while total < 50:
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        total += coin
        if total < 50:
            print(f"Amount Due: {50 - total}")
    else:
        print("Amount Due: 50")

change = total - 50
if change > 0:
    print(f"Change Owed: {change}")
else:
    print(f"Change Owed: {change}")