pay_rate = float(input("Enter your pay rate: "))
hours_worked = float(input("Enter hours worked: "))

if hours_worked > 40:
    overtime_hours = float(input("Enter overtime hours worked: "))
    overtime_hours = pay_rate * 1.5 * overtime_hours
    total_pay = (pay_rate * hours_worked) + overtime_hours
    print(f"Your total pay is ${total_pay: .2f}")
else:
    total_pay = pay_rate * hours_worked
    print(f"Your total pay is ${total_pay: .2f}")