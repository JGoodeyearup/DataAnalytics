student_name = str(input("What is your name? "))
student_major = str(input("What's your major code? "))

match student_major:
    case 'BIOL':
        print(f"Your name is {student_name} and your major is Biology.")
    case 'CSCI':
        print(f"Your name is {student_name} and your major is Computer Science.")
    case 'ENG':
        print(f"Your name is {student_name} and your major is English.")
    case 'HIST':
        print(f"Your name is {student_name} and your major is History.")
    case 'MKT':
        print(f"Your name is {student_name} and your major is Marketing.")
    case _:
        print(f"Please enter a valid major code.")