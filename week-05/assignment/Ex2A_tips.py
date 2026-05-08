# Define Known Values
food_cost = 79.25
tax = 6.54
tip = 12.00
# Calculate Total Cost
total_due = food_cost + tax + tip
print(f"Your total amount is: ${format(total_due, '00.2f')}") # The reason I used the str() function is because I want to use the interger as a string
print(f"Food Cost is ${format(food_cost, '00.2f')} and Tax is ${format(tax, '00.2f')}")
print(f"Your tip is ${format(tip, '00.2f')}")
print(f"Your total amount due is: ${format(total_due, '00.2f')}")