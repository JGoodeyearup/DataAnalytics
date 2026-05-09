a = 10
b = 25
c = 45

if a == max(a, b, c):
    print(f"a is the largest number")
elif b == max(a, b, c):
    print(f"b is the largest number")
else:
    print(f"c is the largest number")

if a == min(a, b, c):
    print(f"a is the smallest number")
elif b == min(a, b, c):
    print(f"b is the smallest number")
else:
    print(f"c is the smallest number")