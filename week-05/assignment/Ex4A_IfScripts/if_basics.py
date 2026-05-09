x = 100
y = 20

if x / y == 5:
    print(f"x divided by y equals 5") 
    x = 1
else:
    print(f"Are varibles set up correctly?")
if x * y == y:
    print(f"Now x times y equals {y}") 
    x = 10
else:
    print(f"Whoops, x equals {x}.")
if x < y:
    print(f"x is less than y")
    x = x * 2
else:
    print(f"Uh oh, x is not less than y.")
if x > y:
    print(f"How is x greater than y??")
else:
    print(f"x is NOT greater than y")

print(f"The final value of x is {x} and the final value of y is {y}.")



