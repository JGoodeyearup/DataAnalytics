import math
import random
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

print(f"Sum of 75 sample values from 1 - 100: {math.fsum(vals_1_100)}")
print(f"The average of 75 sample values: {statistics.mean(vals_sample)}")
print(f"The median of 75 sample values: {statistics.median(vals_sample)}")
print(f"The average of 200 sample values: {statistics.mean(vals_choices)}")
print(f"The median of 200 sample values: {statistics.median(vals_choices)}")
print(f"The mode of 200 sample values: {statistics.mode(vals_choices)}")
print(f"The Standard Deviation of 200 values: {statistics.stdev(vals_choices)}")
print(f"The variance of 200 values: {statistics.variance(vals_choices)}")

radius = float(input("What is the Radius: "))
area = math.floor(pi * (radius ** 2))
area_1 = math.ceil(pi * (radius ** 2))

print(f"The area of your circle rounded down is {area}")
print(f"The are of your circle rounded up is {area_1}")
