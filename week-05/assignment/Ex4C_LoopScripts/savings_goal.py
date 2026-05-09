current_savings = float(input("Enter your current savings: "))
savings_goal = float(input("Enter your savings goal: "))

while current_savings < savings_goal:
    amount_saved = float(input("Enter amount saved: "))
    current_savings += amount_saved
    print(f"Your current savings is ${current_savings: .2f}")
    if current_savings >= savings_goal:
        print(f"Congratulations! You have reached your savings goal of ${current_savings: .2f}!")
    elif current_savings >= (savings_goal / 2):
        print(f"Almost there. This week my balance is ${current_savings: .2f}!")
    elif current_savings >= (savings_goal * 0.75):
        print(f"So Close! After treating myself, my balance is up to {current_savings: .2f}!")
    

