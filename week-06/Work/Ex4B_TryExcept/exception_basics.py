
# ValueError
try:
    first_q = float(input("Enter a Number: "))
    answer = int(first_q) ** 2
    user_inp = fist_q
except ValueError:
    print("Invalid Input. Please Enter a Number.")
except NameError:
    print("OOPS, looks like you tried to assign an undefined object to a variable")
except TypeError:
    print("You've miss classed a variable")
except SyntaxError:
    print("There seems to be an error with your SYNTAX")
else:
    print(f"{user_inp} squared is {answer}")
finally:
    print("Let's Try Again")





#Example:

# try:
#    m = banana
# except NameError:
#    print("NameError: Oops, looks like you tried to assign an undefined object to a variable")
# else:
#     print(m)
# finally:
#    print("Let's try another one...")
