# Define Known Values
food_cost = 79.25
tax = 6.54
tip = 12.00
# Calculate Total Cost
total_due = food_cost + tax + tip
print("Your total amount is: $", str(total_due)) # The reason I used the str() function is because I want to use the interger as a string
print("Food Cost is $" + str(food_cost) + " and Tax is $" + str(tax))
print("Your tip is $" + format(tip, ".2f"))
print("Your total amount due is: $" + str(total_due))