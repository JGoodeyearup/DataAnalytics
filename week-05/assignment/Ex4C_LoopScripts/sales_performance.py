
sales_data = [('Marcus Webb', 'East', 4250.00),
              ('Priya Sharma', 'West', 5875.00),
              ('DeShawn Carter', 'East', 3100.75),
              ('LaTonya Rivers', 'South', 6420.00),
              ('Bob Nyugen', 'West', 4080.25)
             ]
total_amount = 0
for names, region, cash in sales_data:
    total_amount += cash
    if cash < 5000:
        print(f"^ Top performer!")
    print(f"{names} ({region}): {cash}")
print(f"Overall total = {total_amount}")