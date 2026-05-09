
dept_code = int(input("Enter Code for Department: "))
if dept_code == 1:
    print("You have requested for Marketing")
elif dept_code == 5:
    print("You have requested for Human Resources")
elif dept_code == 10:
    print("You have requested for Accounting")
elif dept_code == 12:
    print(f"You have requested for Legal")
elif dept_code == 18:
    print(f"You have requested for IT")
elif dept_code == 20:
    print(f"You have requested for Customer Relations")
else:
    print(f"Please enter a valid department code")