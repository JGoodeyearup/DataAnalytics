import math
area_of_room = float(input("Enter the area of the room in square feet: "))
tile_size = 1 * 0.10
tiles_needed = area_of_room / tile_size
print(f"You will need {math.floor(tiles_needed)} tiles to cover the full room.")