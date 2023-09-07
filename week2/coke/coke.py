paid = 0
cost = 50
accepted_coins = [5,10,25]

while paid < cost:
    coin_inserted = int(input("Insert Coin: "))
    if coin_inserted in accepted_coins:
        paid = paid + coin_inserted
    if paid == cost:
        print ("Change Owed: 0")
    if paid < cost:
        print("Amount Due:", cost-paid)
    if paid > cost:
        print("Change Owed:", paid-cost)
    