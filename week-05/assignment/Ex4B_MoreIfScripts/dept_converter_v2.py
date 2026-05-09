dept_code = int(input("Enter Code for Department: "))
match dept_code:
    case 1:
        print("You have requested for Marketing")
    case 5:
        print("You have requested for Human Resources")
    case 10:
        print("You have requested for Accounting")
    case 12:
        print(f"You have requested for Legal")
    case 18:
        print(f"You have requested for IT")
    case 20:
        print(f"You have requested for Customer Relations")
    case _:
        print(f"Please enter a valid department code")

#  I feel it would be more efficient to use the match 
# case statement because it's easier to read and more 
# straight to the point.

#  The if statement is easier to start with 
# for me because I am more familiar with 
# it but I think the more I use match case 
# the more comfortable I'll be with it. 