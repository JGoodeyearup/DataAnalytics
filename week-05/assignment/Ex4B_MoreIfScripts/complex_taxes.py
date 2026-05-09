pay_rate = float(input("Enter your pay rate: "))
hours_worked = float(input("Enter hours worked: "))
filing_status = str(input("Are you filing as single or joint? "))
yearly_salary = pay_rate * hours_worked * 52

if yearly_salary < 12000 and filing_status == "single":
    tax_rate = 0.05
    weekly_pay
elif yearly_salary >= 12000 and yearly_salary < 24999.99 and filing_status == "single":
    tax_rate = 0.1
elif yearly_salary >= 25000 and yearly_salary < 74999.99 and filing_status == "single":
    tax_rate = 0.15
elif yearly_salary >= 75000 and filing_status == "single":
    tax_rate = 0.2
elif yearly_salary < 12000 and filing_status == "joint":
    tax_rate = 0
elif yearly_salary >= 12000 and yearly_salary < 24999.99 and filing_status == "joint":
    tax_rate = 0.06
elif yearly_salary >= 25000 and yearly_salary < 74999.99 and filing_status == "joint":
    tax_rate = 0.11
elif yearly_salary >= 75000 and filing_status == "joint":
    tax_rate = 0.20
print(f"You worked {hours_worked} hours this period. "
      f"\nBecause you earned ${pay_rate} per hour, " 
      f"\nyour gross weekly pay is ${pay_rate * hours_worked: .2f}. "
      f"\nYour filing status is {filing_status}. "
      f"\nYour tax withholding for the week is ${pay_rate * hours_worked * tax_rate: .2f}. "
      f"\nYour net pay is ${pay_rate * hours_worked * (1 - tax_rate): .2f}.")