
from datetime import datetime, time

user_input = input("What time is it? (hh:mm am/pm): ").strip().lower()

# Parse 12-hour time
current_time = datetime.strptime(user_input, "%I:%M %p").time()

if time(5, 0) <= current_time < time(10, 0):
    print("Good morning!")
elif time(10, 0) <= current_time < time(17, 0):
    print("Good day!")
elif time(17, 0) <= current_time < time(23, 0):
    print("Good evening!")
else:
    print("What are you doing up so late?")

