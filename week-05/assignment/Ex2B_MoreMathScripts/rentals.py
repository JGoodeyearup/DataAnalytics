
import math
tour_size = int(input("Enter the size of the tour group: "))
van = 15
van_cost = 250
vans_needed = math.ceil(tour_size / van)
total_cost = vans_needed * van_cost 
per_person_cost = total_cost / tour_size 
print(f"You will need {vans_needed} vans to support a tour group of {tour_size} people.")
print(f"The total cost of the vans will be ${format(total_cost, '.2f')}.")
print(f"The cost per person will be ${format(per_person_cost, '.2f')}")
