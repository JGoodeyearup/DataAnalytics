def mail_label(name, address, city, state, zipcode):
    print(f"{name} \n{address} {city}, {state} \n{zipcode}")

person = str(input("What's Your Name: "))
street = input("What Street do You Reside: ")
area = str(input("What City do You Reside: "))
location = str(input("What State do You Reside: "))
postal_code = int(input("Whats Your Zipcode: "))

mail_label(person, street, area, location, postal_code)

def add_number(number, number2, number3):
    print(number + number2 + number3)
    
a = int(input("Enter the First #: "))
b = int(input("Enter the Second #: "))
c = int(input("Enter the Last #: "))

add_number(a, b, c)


def display_recipt(total_due, amount_paid, change):
    print(f"Total Amount:${total_due} \nAmount Paid:${amount_paid} \nChange_Due:${change}")

due = float(input("How much does customer owe:$ "))
paid = float(input("How much did they pay:$ "))
change = paid - due
display_recipt(due, paid, change)
