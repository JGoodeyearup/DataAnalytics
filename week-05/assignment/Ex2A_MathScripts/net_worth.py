# net worth = how much you have - how much you owe
# assets = stuff you own in cash value
# debt = stuff you owe in cash value

car = 60000
house = 2000000
credit_card_debt = 15000

assets = car + house 
debt = credit_card_debt
net_worth = assets - debt
print("Your net worth is: $" + format(net_worth, ",.2f"))
