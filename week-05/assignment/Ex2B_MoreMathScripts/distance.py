import math
p1 = (int(input("Enter the x coordinate of P1: ")), int(input("Enter the y coordinate of P1: ")))
p2 = (int(input("Enter the x coordinate of P2: ")), int(input("Enter the y coordinate of P2: ")))
distance = math.dist(p1, p2)
print(f"The distance between the points {p1} and {p2} is {format(distance, '.2f')}")